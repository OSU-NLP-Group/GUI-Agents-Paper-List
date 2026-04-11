import os
import shutil
import re
import sys
import logging
import calendar
from collections import Counter

import pandas as pd
import matplotlib
from wordcloud import WordCloud

# Force a non-interactive backend so generation works in headless environments.
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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

    # Generate a truncated recent papers list for README (to stay under GitHub's 512KB render limit)
    max_recent_papers = 500
    recent_df = papers_df.head(max_recent_papers)
    recent_markdown = "\n".join(df_to_markdown_list(recent_df))
    write_file("update_template_or_data/recent_paper_list.md", recent_markdown)

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
        grouped_authors_markdown = []
        for author, count in top_authors_sorted:
            author_filename = f"paper_{author.replace(' ', '_')}.md"
            author_link = f"paper_by_author/{author_filename}"
            grouped_authors_markdown.append(f"[{author} ({count})]({author_link}) | ")
        grouped_authors_markdown_str = "".join(grouped_authors_markdown).rstrip(" | ")
        write_file("update_template_or_data/author_grouping.md", grouped_authors_markdown_str)
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

        # Generate env grouping markdown table with counts
        header_cells = [f"[{env_key} ({env_counts[env_key]})](paper_by_env/{file_name})"
                        for env_key, file_name in env_keywords.items()]
        env_header = "| " + " | ".join(header_cells) + " |"
        env_separator = "|" + "|".join(["---"] * len(env_keywords)) + "|"
        write_file("update_template_or_data/env_grouping.md", env_header + "\n" + env_separator)
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

        grouped_keywords_markdown = []
        for keyword, count in combined_keywords:
            keyword_filename = f"paper_{keyword.replace(' ', '_')}.md"
            keyword_link = f"paper_by_key/{keyword_filename}"
            grouped_keywords_markdown.append(f"[{keyword} ({count})]({keyword_link}) | ")
        grouped_keywords_markdown_str = "".join(grouped_keywords_markdown).rstrip(" | ")
        write_file("update_template_or_data/keyword_grouping.md", grouped_keywords_markdown_str)
    except Exception as e:
        logging.error(f"Error generating sorted keyword grouping Markdown: {str(e)}", exc_info=True)

    # --- Generate keyword word cloud ---
    try:
        wordcloud = WordCloud(
            width=2000, height=1000, background_color="white",
            max_font_size=140, min_font_size=10
        ).generate_from_frequencies(keyword_counts)
        plt.figure(figsize=(20, 10))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.savefig("update_template_or_data/statistics/keyword_wordcloud_long.png", dpi=400)
        plt.close()
    except Exception as e:
        logging.error(f"Error generating keyword word cloud: {str(e)}", exc_info=True)

    # --- Final summary ---
    if _warnings:
        print(f"\n{len(_warnings)} warning(s) during processing:", file=sys.stderr)
        for w in _warnings:
            print(f"  - {w}", file=sys.stderr)


if __name__ == "__main__":
    process_markdown()
