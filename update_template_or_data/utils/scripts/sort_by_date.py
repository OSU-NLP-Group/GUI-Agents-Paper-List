import os
import pandas as pd
import calendar
import re
import logging
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

# Configure logging
log_dir = "update_template_or_data/logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
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
            parsed_date = parser.parse(date_str, fuzzy=True, default=pd.Timestamp.now())
            last_day = calendar.monthrange(parsed_date.year, parsed_date.month)[1]
            return pd.Timestamp(year=parsed_date.year, month=parsed_date.month, day=last_day)
        except ValueError:
            try:
                year = int(re.search(r"\b(20\d{2})\b", date_str).group(0))
                return pd.Timestamp(year=year, month=12, day=31)
            except (ValueError, AttributeError):
                return pd.NaT

# Main logic
@safe_execute
def process_markdown():
    """Processes markdown input, generates categorized outputs, and saves data"""
    paper_source = "update_template_or_data/update_paper_list.md"
    sample_input = read_file(paper_source)

    if sample_input is None:
        return  # If file reading failed, exit early

    new_format_pattern = re.compile(
        r"- \[(.*?)\]\((.*?)\)\s+"
        r"- (.*?)\s+"
        r"- 🏛️ Institutions: (.*?)\s+"
        r"- 📅 Date: (.*?)\s+"
        r"- 📑 Publisher: (.*?)\s+"
        r"- 💻 Env: \[(.*?)\]\s+"
        r"- 🔑 Key: (.*?)\s+"
        r"- 📖 TLDR: (.*?)\n",
        re.DOTALL
    )

    parsed_entries = []
    for match in new_format_pattern.findall(sample_input):
        try:
            title, link, authors, institutions, date, publisher, env, keywords, tldr = match
            parsed_date = parse_date_with_defaults(date)
            formatted_keywords = ", ".join([f"{kw.strip()}" for kw in keywords.split(",")])
            parsed_entries.append((title, link, authors, institutions, date, parsed_date, publisher, f"[{env.strip()}]",
                                   formatted_keywords, tldr))
        except Exception as e:
            logging.error(f"Error parsing entry: {str(e)}", exc_info=True)

    papers_df = pd.DataFrame(parsed_entries, columns=[
        'Title', 'Link', 'Authors', 'Institutions', 'Original Date', 'Parsed Date', 'Publisher', 'Env', 'Keywords', 'TLDR'
    ]).drop_duplicates(subset='Title', keep='first')
    papers_df.sort_values(by='Parsed Date', ascending=False, inplace=True)

    sorted_markdown = []
    for _, row in papers_df.iterrows():
        markdown_entry = f"- [{row['Title']}]({row['Link']})\n" \
                         f"    - {row['Authors']}\n" \
                         f"    - 🏛️ Institutions: {row['Institutions']}\n" \
                         f"    - 📅 Date: {row['Original Date']}\n" \
                         f"    - 📑 Publisher: {row['Publisher']}\n" \
                         f"    - 💻 Env: {row['Env']}\n" \
                         f"    - 🔑 Key: {row['Keywords']}\n" \
                         f"    - 📖 TLDR: {row['TLDR']}\n"
        sorted_markdown.append(markdown_entry)

    final_output = "\n".join(sorted_markdown)
    write_file("update_template_or_data/update_paper_list.md", final_output)

    # Generate top authors chart
    try:
        author_counter = Counter()
        for _, row in papers_df.iterrows():
            authors = row['Authors']
            author_list = [author.strip() for author in authors.split(',')]
            author_counter.update(author_list)

        num_top_author = 10
        top_authors = [author for author, _ in author_counter.most_common(num_top_author)]
        top_15_counts = [author_counter[author] for author in top_authors]

        plt.figure(figsize=(10, 10))
        sns.barplot(x=top_15_counts, y=top_authors, palette="viridis")

        plt.title("Top Authors by Number of Papers", fontsize=20)
        plt.xlabel("Number of Papers", fontsize=20)
        plt.ylabel("Authors", fontsize=20)

        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.tight_layout()
        plt.savefig("update_template_or_data/statistics/top_authors.png")
    except Exception as e:
        logging.error(f"Error generating top authors chart: {str(e)}", exc_info=True)

    # Generate keyword word cloud
    try:
        all_keywords = []
        for _, row in papers_df.iterrows():
            keywords = row['Keywords']
            filtered_keywords = [kw.strip() for kw in keywords.split(",") if kw.strip()]
            all_keywords.extend(filtered_keywords)
        keyword_counts = Counter(all_keywords)
        wordcloud = WordCloud(
            width=1000, height=1000, background_color="white"
        ).generate_from_frequencies(keyword_counts)
        plt.figure(figsize=(10, 10))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.savefig("update_template_or_data/statistics/keyword_wordcloud.png", dpi=460)
        plt.close()
    except Exception as e:
        logging.error(f"Error generating keyword word cloud: {str(e)}", exc_info=True)

if __name__ == "__main__":
    process_markdown()