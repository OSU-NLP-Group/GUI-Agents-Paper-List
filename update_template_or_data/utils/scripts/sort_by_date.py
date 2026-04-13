import os
import shutil
import re
import sys
import logging
import calendar
from collections import Counter

import pandas as pd

# Configure logging
log_dir = "update_template_or_data/logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "error.log")
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Track parse warnings for summary at end
_warnings = []


def warn(msg):
    """Print a warning and record it for the final summary."""
    _warnings.append(msg)
    print(f"  WARNING: {msg}", file=sys.stderr)


def read_file(filepath, encoding="utf-8"):
    """Reads a file and returns its content."""
    with open(filepath, "r", encoding=encoding) as file:
        return file.read()


def write_file(filepath, content, encoding="utf-8"):
    """Writes content to a file."""
    with open(filepath, "w", encoding=encoding) as file:
        file.write(content)


def parse_date_with_defaults(date_str):
    """Parses dates with default values for incomplete or malformed dates."""
    try:
        result = pd.to_datetime(date_str, errors='coerce')
        if pd.notna(result):
            return result
    except ValueError:
        pass
    # Try to extract just a year
    try:
        year = int(re.search(r"\b(20\d{2})\b", date_str).group(0))
        return pd.Timestamp(year=year, month=12, day=31)
    except (ValueError, AttributeError):
        return pd.NaT


def normalize_date_str(date_str, parsed_date):
    """Normalize date string to canonical format.

    - Full dates → 'Month DD, YYYY' (e.g., 'October 30, 2024')
    - Month-only dates (e.g., 'November 2024') → kept as 'Month YYYY'
      but internally sorted using last day of that month.
    """
    if pd.isna(parsed_date):
        return date_str  # Can't normalize, keep original

    # Check if original was month-only (no day)
    if re.match(r'^[A-Za-z]+ \d{4}$', date_str.strip()):
        # Keep as "Month YYYY" to indicate day is unknown
        return parsed_date.strftime('%B') + ' ' + str(parsed_date.year)

    return parsed_date.strftime('%B %d, %Y')


def parse_date_for_sorting(date_str):
    """Parse date for sorting. Month-only dates use last day of month."""
    parsed = parse_date_with_defaults(date_str)
    if pd.isna(parsed):
        return parsed

    # If month-only, use last day for sorting
    if re.match(r'^[A-Za-z]+ \d{4}$', date_str.strip()):
        last_day = calendar.monthrange(parsed.year, parsed.month)[1]
        return pd.Timestamp(year=parsed.year, month=parsed.month, day=last_day)

    return parsed


def clear_folder(folder_path):
    """Remove all files and subdirectories inside folder_path."""
    if not os.path.exists(folder_path):
        return
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)


def extract_keywords(keywords_str):
    """Extract individual keywords from a Keywords field, stripping [] brackets."""
    return [re.sub(r'^\[|\]$', '', kw.strip()) for kw in keywords_str.split(",") if kw.strip()]


def has_keyword(keywords_str, target):
    """Check if a specific keyword exists as an exact token in the Keywords field."""
    return target.lower() in [kw.lower() for kw in extract_keywords(keywords_str)]


def has_author(authors_str, target):
    """Check if a specific author exists as an exact name in the Authors field."""
    author_list = [a.strip().lower() for a in authors_str.split(',')]
    return target.strip().lower() in author_list


def build_markdown_entry(row):
    """Build a markdown entry string from a DataFrame row."""
    return (
        f"- [{row['Title']}]({row['Link']})\n"
        f"    - {row['Authors']}\n"
        f"    - \U0001f3db\ufe0f Institutions: {row['Institutions']}\n"
        f"    - \U0001f4c5 Date: {row['Original Date']}\n"
        f"    - \U0001f4d1 Publisher: {row['Publisher']}\n"
        f"    - \U0001f4bb Env: {row['Env']}\n"
        f"    - \U0001f511 Key: {row['Keywords']}\n"
        f"    - \U0001f4d6 TLDR: {row['TLDR']}\n"
    )


def df_to_markdown_list(df):
    """Convert a DataFrame to a list of markdown entry strings."""
    return [build_markdown_entry(row) for _, row in df.iterrows()]


def filter_by_keyword(df, keyword):
    """Filter DataFrame to rows containing an exact keyword match."""
    return df[df['Keywords'].apply(lambda kws: has_keyword(kws, keyword))]


def filter_by_author(df, author):
    """Filter DataFrame to rows containing an exact author match."""
    return df[df['Authors'].apply(lambda authors: has_author(authors, author))]


def build_empty_env_page(env_key):
    """Build fallback content for an empty environment grouping page."""
    return f"# {env_key} Papers\n\nNo papers currently tagged with [{env_key}].\n"


# Main logic
def process_markdown():
    """Processes markdown input, generates categorized outputs, and saves data."""
    paper_source = "ALL_PAPERS.md"
    sample_input = read_file(paper_source)

    # Env field supports single [Web] or multi [Desktop], [Web]
    new_format_pattern = re.compile(
        r"- \[(.*?)\]\((.*?)\)\s+"
        r"- (.*?)\s+"
        r"- \U0001f3db\ufe0f Institutions: (.*?)\s+"
        r"- \U0001f4c5 Date: (.*?)\s+"
        r"- \U0001f4d1 Publisher: (.*?)\s+"
        r"- \U0001f4bb Env: (\[.*?\](?:, \[.*?\])*)\s+"
        r"- \U0001f511 Key: (.*?)\s+"
        r"- \U0001f4d6 TLDR: (.*?)\n",
        re.DOTALL
    )

    # Count raw entries (lines starting with "- [") to detect parse failures
    raw_entry_count = len(re.findall(r'^- \[', sample_input, re.MULTILINE))

    parsed_entries = []
    for match in new_format_pattern.findall(sample_input):
        try:
            title, link, authors, institutions, date, publisher, env, keywords, tldr = match
            parsed_date = parse_date_for_sorting(date.strip())
            normalized_date = normalize_date_str(date.strip(), parsed_date)
            formatted_keywords = ", ".join([kw.strip() for kw in keywords.split(",")])

            if pd.isna(parsed_date):
                warn(f"Unparseable date '{date.strip()}' for paper: {title}")

            parsed_entries.append((
                title, link, authors, institutions, normalized_date, parsed_date,
                publisher, env.strip(), formatted_keywords, tldr
            ))
        except Exception as e:
            logging.error(f"Error parsing entry: {str(e)}", exc_info=True)
            warn(f"Failed to parse entry: {str(e)}")

    parsed_count = len(parsed_entries)
    dropped = raw_entry_count - parsed_count
    if dropped > 0:
        warn(f"{dropped} entries failed to parse (out of {raw_entry_count} total)")

    papers_df = pd.DataFrame(parsed_entries, columns=[
        'Title', 'Link', 'Authors', 'Institutions', 'Original Date',
        'Parsed Date', 'Publisher', 'Env', 'Keywords', 'TLDR'
    ])

    dupes = papers_df.duplicated(subset='Title', keep='first').sum()
    if dupes > 0:
        warn(f"{dupes} duplicate title(s) removed")
    papers_df = papers_df.drop_duplicates(subset='Title', keep='first')
    papers_df.sort_values(by='Parsed Date', ascending=False, inplace=True)

    print(f"Processed {len(papers_df)} papers successfully.")

    # Write full sorted paper list back to ALL_PAPERS.md (source of truth)
    all_papers_markdown = df_to_markdown_list(papers_df)
    final_output = "\n".join(all_papers_markdown)
    write_file("ALL_PAPERS.md", final_output)

    # Write paper count fragment for README template
    total_papers = len(papers_df)
    write_file("update_template_or_data/paper_count.md", str(total_papers))

    # Generate the paper list section for README.
    # Truncate to 500 papers if needed (GitHub truncates README rendering at ~512KB).
    max_readme_papers = 500
    is_truncated = total_papers > max_readme_papers
    display_df = papers_df.head(max_readme_papers) if is_truncated else papers_df
    paper_entries = "\n".join(df_to_markdown_list(display_df))

    section_lines = []
    section_lines.append(
        "> Adjacent but non-canonical papers that are heavily reused in GUI research "
        "can be curated separately in [ADJACENT_PAPERS.md](ADJACENT_PAPERS.md)."
    )
    if is_truncated:
        section_lines.append(">")
        section_lines.append(
            f"> **Full list**: [ALL_PAPERS.md](ALL_PAPERS.md) — "
            f"This README shows the {max_readme_papers} most recent papers only."
        )
    section_lines.append("")
    if is_truncated:
        section_lines.append("## Recent Papers (from most recent to oldest)")
    else:
        section_lines.append("## All Papers (from most recent to oldest)")
    section_lines.append("")
    section_lines.append(paper_entries)

    write_file("update_template_or_data/paper_list_section.md", "\n".join(section_lines))

    # Clear and recreate output directories
    for folder in ["update_template_or_data/statistics/", "paper_by_key",
                    "paper_by_env", "paper_by_author"]:
        clear_folder(folder)
    os.makedirs("update_template_or_data/statistics/", exist_ok=True)

    # Count authors once for reuse (exact name matching)
    author_counter = Counter()
    for _, row in papers_df.iterrows():
        author_list = [a.strip() for a in row['Authors'].split(',')]
        author_counter.update(author_list)

    top_num_author = 20
    top_authors_sorted = sorted(author_counter.items(), key=lambda x: x[1], reverse=True)[:top_num_author]

    # Count keywords once for reuse (exact token matching)
    all_keywords = []
    for _, row in papers_df.iterrows():
        all_keywords.extend(extract_keywords(row['Keywords']))
    keyword_counts = Counter(all_keywords)

    # --- Generate author grouping markdown ---
    try:
        # Generate author grouping as dot-separated links, 5 per line
        author_links = []
        for author, count in top_authors_sorted:
            a_file = f"paper_{author.replace(' ', '_')}.md"
            author_links.append(f"[{author} ({count})](paper_by_author/{a_file})")
        per_line = 5
        author_lines = []
        for i in range(0, len(author_links), per_line):
            author_lines.append(" · ".join(author_links[i:i+per_line]))
        write_file("update_template_or_data/author_grouping.md",
                    "<br>".join(author_lines))
    except Exception as e:
        logging.error(f"Error generating sorted author grouping Markdown: {str(e)}", exc_info=True)

    # --- Generate author-specific files ---
    try:
        os.makedirs("paper_by_author", exist_ok=True)
        top_author_names = [author for author, _ in top_authors_sorted]
        for author in top_author_names:
            filtered_df = filter_by_author(papers_df, author)
            if not filtered_df.empty:
                entries = "\n".join(df_to_markdown_list(filtered_df))
                author_filename = f"paper_{author.replace(' ', '_')}.md"
                write_file(os.path.join("paper_by_author", author_filename),
                           f"# {author}'s Papers\n\n{entries}")
    except Exception as e:
        logging.error(f"Error generating author-specific files: {str(e)}", exc_info=True)

    # --- Generate environment-specific files ---
    try:
        os.makedirs("paper_by_env", exist_ok=True)
        env_keywords = {
            "Web": "paper_web.md",
            "Desktop": "paper_desktop.md",
            "Mobile": "paper_mobile.md",
            "General GUI": "paper_general_gui.md",
        }
        legacy_env_files = {"paper_gui.md", "paper_search.md", "paper_misc.md"}
        for legacy_file in legacy_env_files:
            legacy_path = os.path.join("paper_by_env", legacy_file)
            if os.path.exists(legacy_path):
                os.remove(legacy_path)
        env_counts = {}
        for env_key, file_name in env_keywords.items():
            # Env field uses [brackets], so match the exact bracket token
            filtered_df = papers_df[papers_df['Env'].str.contains(rf'\[{env_key}\]', case=False, na=False, regex=True)]
            env_counts[env_key] = len(filtered_df)
            if not filtered_df.empty:
                entries = "\n".join(df_to_markdown_list(filtered_df))
            else:
                entries = build_empty_env_page(env_key)
            write_file(os.path.join("paper_by_env", file_name), entries)

        # Generate env grouping as emoji links on one line
        env_emoji = {"Web": "🌐", "Desktop": "🖥️", "Mobile": "📱", "General GUI": "🖼️"}
        env_parts = []
        for env_key, file_name in env_keywords.items():
            emoji = env_emoji.get(env_key, "")
            count = env_counts[env_key]
            env_parts.append(f"{emoji} [{env_key} ({count})](paper_by_env/{file_name})")
        write_file("update_template_or_data/env_grouping.md", " · ".join(env_parts))
    except Exception as e:
        logging.error(f"Error generating environment-specific files: {str(e)}", exc_info=True)

    # --- Generate keyword-specific files ---
    try:
        predefined_keywords = {"framework", "dataset", "benchmark", "model", "safety", "survey"}
        top_keywords = [
            kw for kw, _ in keyword_counts.most_common()
            if kw not in predefined_keywords
        ][:14]
        keywords_to_group = predefined_keywords.union(top_keywords)

        os.makedirs("paper_by_key", exist_ok=True)
        for keyword in keywords_to_group:
            filtered_df = filter_by_keyword(papers_df, keyword)
            if not filtered_df.empty:
                entries = "\n".join(df_to_markdown_list(filtered_df))
                file_path = os.path.join("paper_by_key", f"paper_{keyword.replace(' ', '_')}.md")
                write_file(file_path, f"# Papers with Keyword: {keyword}\n\n{entries}")
    except Exception as e:
        logging.error(f"Error generating keyword-based Markdown files: {str(e)}", exc_info=True)

    # --- Generate keyword grouping markdown ---
    try:
        predefined_keywords_list = ["model", "framework", "benchmark", "dataset", "safety", "survey"]
        predefined_keyword_counts = [(kw, keyword_counts[kw]) for kw in predefined_keywords_list if kw in keyword_counts]
        remaining_keywords = [
            (kw, count) for kw, count in keyword_counts.most_common()
            if kw not in predefined_keywords_list
        ]
        top_num_keywords = 20 - len(predefined_keywords_list)
        top_remaining_keywords = remaining_keywords[:top_num_keywords]
        combined_keywords = predefined_keyword_counts + top_remaining_keywords
        combined_keywords.sort(
            key=lambda x: (-x[1], predefined_keywords_list.index(x[0]) if x[0] in predefined_keywords_list else float('inf')))

        # Generate keyword grouping as dot-separated links, 5 per line
        kw_links = []
        for keyword, count in combined_keywords:
            kw_file = f"paper_{keyword.replace(' ', '_')}.md"
            kw_links.append(f"[{keyword} ({count})](paper_by_key/{kw_file})")
        per_line = 5
        kw_lines = []
        for i in range(0, len(kw_links), per_line):
            kw_lines.append(" · ".join(kw_links[i:i+per_line]))
        write_file("update_template_or_data/keyword_grouping.md",
                    "<br>".join(kw_lines))
    except Exception as e:
        logging.error(f"Error generating sorted keyword grouping Markdown: {str(e)}", exc_info=True)

    # --- Generate keyword bar chart ---
    try:
        try:
            import plotly.graph_objects as go
            _has_plotly_kw = True
        except ImportError:
            _has_plotly_kw = False

        if _has_plotly_kw:
            top_kw = keyword_counts.most_common(25)
            top_kw.reverse()
            kw_labels = [k for k, _ in top_kw]
            kw_values = [v for _, v in top_kw]

            fig_kw = go.Figure()
            fig_kw.add_trace(go.Bar(
                y=kw_labels, x=kw_values, orientation='h',
                text=kw_values, textposition='outside',
                textfont=dict(size=12, color='#444'),
                marker=dict(
                    color=kw_values,
                    colorscale=[[0, '#BFDBFE'], [0.4, '#3B82F6'], [1, '#1E3A8A']],
                    line=dict(width=0), cornerradius=3,
                ),
            ))
            fig_kw.update_layout(
                title=dict(text='Top 25 Research Keywords',
                           font=dict(size=20, color='#1a1a1a'), x=0.5),
                xaxis=dict(
                    title=dict(text='Number of papers', font=dict(size=13, color='#666')),
                    gridcolor='rgba(0,0,0,0.06)', zeroline=False,
                    tickfont=dict(size=11, color='#888'),
                    range=[0, max(kw_values) * 1.15],
                ),
                yaxis=dict(tickfont=dict(size=12, color='#444'), showgrid=False),
                plot_bgcolor='white', paper_bgcolor='white', showlegend=False,
                margin=dict(l=160, r=50, t=60, b=50),
                width=900, height=650, bargap=0.25,
            )
            fig_kw.write_image(
                'update_template_or_data/statistics/keyword_bar_chart.png', scale=2)
        else:
            warn("plotly not installed, skipping keyword bar chart")
    except Exception as e:
        logging.error(f"Error generating keyword bar chart: {str(e)}", exc_info=True)

    # --- Generate quarterly publication trend chart ---
    try:
        import numpy as np
        try:
            import plotly.graph_objects as go
            _has_plotly = True
        except ImportError:
            _has_plotly = False

        if _has_plotly:
            trend_df = papers_df[papers_df['Parsed Date'] >= '2023-01-01'].copy()
            trend_df['quarter'] = trend_df['Parsed Date'].dt.to_period('Q')
            quarterly = trend_df.groupby('quarter').size().reset_index(name='count')
            quarterly['mid_date'] = quarterly['quarter'].apply(
                lambda q: q.start_time + pd.Timedelta(days=45))
            quarterly['label'] = quarterly['quarter'].apply(
                lambda q: f"Q{q.quarter} {q.year}")
            counts = quarterly['count'].values

            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=quarterly['mid_date'], y=counts,
                text=counts, textposition='outside',
                textfont=dict(size=13, color='#333'),
                width=60 * 86400000,
                marker=dict(
                    color=counts,
                    colorscale=[[0, '#93C5FD'], [0.5, '#3B82F6'], [1, '#1D4ED8']],
                    line=dict(width=0), cornerradius=4,
                ),
                hovertemplate='<b>%{customdata}</b><br>%{y} papers<extra></extra>',
                customdata=quarterly['label'],
            ))
            fig.update_layout(
                title=dict(
                    text='GUI Agent Research: Quarterly Publication Trend',
                    font=dict(size=22, color='#1a1a1a'), x=0.5,
                ),
                yaxis=dict(
                    title=dict(text='Papers per quarter', font=dict(size=14, color='#666')),
                    gridcolor='rgba(0,0,0,0.06)', zeroline=False,
                    tickfont=dict(size=11, color='#888'),
                    range=[0, max(counts) * 1.22],
                ),
                xaxis=dict(
                    tickfont=dict(size=11, color='#666'), showgrid=False,
                    tickvals=quarterly['mid_date'], ticktext=quarterly['label'],
                    tickangle=0,
                ),
                plot_bgcolor='white', paper_bgcolor='white',
                showlegend=False,
                margin=dict(l=60, r=30, t=70, b=50),
                width=1100, height=480, bargap=0.3,
            )
            fig.write_image(
                'update_template_or_data/statistics/quarterly_trend.png', scale=2)
        else:
            warn("plotly not installed, skipping quarterly trend chart")
    except Exception as e:
        logging.error(f"Error generating quarterly trend chart: {str(e)}", exc_info=True)

    # --- Final summary ---
    if _warnings:
        print(f"\n{len(_warnings)} warning(s) during processing:", file=sys.stderr)
        for w in _warnings:
            print(f"  - {w}", file=sys.stderr)


if __name__ == "__main__":
    process_markdown()
