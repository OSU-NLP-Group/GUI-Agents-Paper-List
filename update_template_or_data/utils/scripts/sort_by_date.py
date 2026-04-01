import os
import shutil
import re
import logging
from collections import Counter

import pandas as pd
from wordcloud import WordCloud
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


def safe_execute(func):
    """Decorator to catch exceptions and log them"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {str(e)}", exc_info=True)
    return wrapper


@safe_execute
def read_file(filepath, encoding="utf-8"):
    """Reads a file and returns its content"""
    with open(filepath, "r", encoding=encoding) as file:
        return file.read()


@safe_execute
def write_file(filepath, content, encoding="utf-8"):
    """Writes content to a file"""
    with open(filepath, "w", encoding=encoding) as file:
        file.write(content)


@safe_execute
def parse_date_with_defaults(date_str):
    """Parses dates with default values for incomplete or malformed dates"""
    try:
        return pd.to_datetime(date_str, errors='coerce')
    except ValueError:
        try:
            year = int(re.search(r"\b(20\d{2})\b", date_str).group(0))
            return pd.Timestamp(year=year, month=12, day=31)
        except (ValueError, AttributeError):
            return pd.NaT


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


def remove_square_brackets(s):
    """Remove leading '[' and trailing ']' from a string."""
    return re.sub(r'^\[|\]$', '', s)


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


# Main logic
@safe_execute
def process_markdown():
    """Processes markdown input, generates categorized outputs, and saves data"""
    paper_source = "update_template_or_data/update_paper_list.md"
    sample_input = read_file(paper_source)

    if sample_input is None:
        return  # If file reading failed, exit early

    # Env field supports single [Web] or multi [Web], [Search]
    new_format_pattern = re.compile(
        r"- \[(.*?)\]\((.*?)\)\s+"
        r"- (.*?)\s+"
        r"- 🏛️ Institutions: (.*?)\s+"
        r"- 📅 Date: (.*?)\s+"
        r"- 📑 Publisher: (.*?)\s+"
        r"- 💻 Env: (\[.*?\](?:, \[.*?\])*)\s+"
        r"- 🔑 Key: (.*?)\s+"
        r"- 📖 TLDR: (.*?)\n",
        re.DOTALL
    )

    parsed_entries = []
    for match in new_format_pattern.findall(sample_input):
        try:
            title, link, authors, institutions, date, publisher, env, keywords, tldr = match
            parsed_date = parse_date_with_defaults(date)
            formatted_keywords = ", ".join([kw.strip() for kw in keywords.split(",")])
            parsed_entries.append((
                title, link, authors, institutions, date, parsed_date,
                publisher, env.strip(), formatted_keywords, tldr
            ))
        except Exception as e:
            logging.error(f"Error parsing entry: {str(e)}", exc_info=True)

    papers_df = pd.DataFrame(parsed_entries, columns=[
        'Title', 'Link', 'Authors', 'Institutions', 'Original Date',
        'Parsed Date', 'Publisher', 'Env', 'Keywords', 'TLDR'
    ]).drop_duplicates(subset='Title', keep='first')
    papers_df.sort_values(by='Parsed Date', ascending=False, inplace=True)

    # Write sorted paper list back
    final_output = "\n".join(df_to_markdown_list(papers_df))
    write_file("update_template_or_data/update_paper_list.md", final_output)

    # Clear and recreate output directories
    for folder in ["update_template_or_data/statistics/", "paper_by_key",
                    "paper_by_env", "paper_by_author"]:
        clear_folder(folder)
    os.makedirs("update_template_or_data/statistics/", exist_ok=True)

    # Count authors once for reuse
    author_counter = Counter()
    for _, row in papers_df.iterrows():
        author_list = [a.strip() for a in row['Authors'].split(',')]
        author_counter.update(author_list)

    top_num_author = 20
    top_authors_sorted = sorted(author_counter.items(), key=lambda x: x[1], reverse=True)[:top_num_author]

    # Count keywords once for reuse
    all_keywords = []
    for _, row in papers_df.iterrows():
        filtered = [remove_square_brackets(kw.strip()) for kw in row['Keywords'].split(",") if kw.strip()]
        all_keywords.extend(filtered)
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
            filtered_df = papers_df[papers_df['Authors'].str.contains(author, case=False, na=False)]
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
            "GUI": "paper_gui.md",
            "Search": "paper_search.md",
            "Misc": "paper_misc.md",
        }
        for env_key, file_name in env_keywords.items():
            filtered_df = papers_df[papers_df['Env'].str.contains(env_key, case=False, na=False)]
            if not filtered_df.empty:
                entries = "\n".join(df_to_markdown_list(filtered_df))
                write_file(os.path.join("paper_by_env", file_name), entries)
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
            filtered_df = papers_df[papers_df['Keywords'].str.contains(keyword, case=False, na=False)]
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


if __name__ == "__main__":
    process_markdown()
