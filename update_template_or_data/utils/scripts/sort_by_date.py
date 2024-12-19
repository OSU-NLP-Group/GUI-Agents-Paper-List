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

    import shutil

    def clear_folder(folder_path):
        try:
            # 检查文件夹是否存在
            if not os.path.exists(folder_path):
                print(f"文件夹 '{folder_path}' 不存在！")
                return

            # 遍历文件夹中的所有文件和子文件夹
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)

                # 如果是文件，删除文件
                if os.path.isfile(item_path):
                    os.remove(item_path)

                # 如果是文件夹，删除整个文件夹
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)

            print(f"文件夹 '{folder_path}' 已成功清空！")

        except Exception as e:
            print(f"清空文件夹时出错: {e}")

    folder_to_clear = "update_template_or_data/statistics/"
    clear_folder(folder_to_clear)
    subgroup_dir="update_template_or_data/statistics/"
    if not os.path.exists(subgroup_dir):
        os.makedirs(subgroup_dir)


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

    def remove_square_brackets(s):
        # 使用正则表达式去除开头和结尾的方括号
        return re.sub(r'^\[|\]$', '', s)

    # Generate Markdown files grouped by keywords
    try:
        predefined_keywords = {"framework", "dataset", "benchmark", "model", "safety", "survey"}

        # Calculate keyword frequencies
        all_keywords = []
        for _, row in papers_df.iterrows():
            keywords = row['Keywords']
            filtered_keywords = [remove_square_brackets(kw.strip()) for kw in keywords.split(",") if kw.strip()]
            all_keywords.extend(filtered_keywords)
        keyword_counts = Counter(all_keywords)

        # Determine top 5 most frequent keywords excluding predefined ones
        top_keywords = [
                           keyword for keyword, _ in keyword_counts.most_common()
                           if keyword not in predefined_keywords
                       ][:14]

        # Combine predefined keywords with the top 5
        keywords_to_group = predefined_keywords.union(top_keywords)

        # Create directory for keyword-based grouping


        # 使用示例
        folder_to_clear = "paper_by_key"
        clear_folder(folder_to_clear)

        folder_to_clear = "paper_by_env"
        clear_folder(folder_to_clear)

        folder_to_clear = "paper_by_author"
        clear_folder(folder_to_clear)

        # Generate sorted author grouping markdown
        # Generate sorted author grouping markdown
        try:
            # Count authors across papers
            author_counter = Counter()
            for _, row in papers_df.iterrows():
                authors = row['Authors']
                author_list = [author.strip() for author in authors.split(',')]
                author_counter.update(author_list)

            # Sort authors by the number of papers in descending order
            sorted_authors = sorted(author_counter.items(), key=lambda x: x[1], reverse=True)

            # Limit to top N authors
            top_num_author = 20  # Change this number to adjust how many authors to keep
            top_authors = sorted_authors[:top_num_author]

            # Generate Markdown content for the top authors
            grouped_authors_markdown = []
            for author, count in top_authors:
                author_filename = f"paper_{author.replace(' ', '_')}.md"
                author_link = f"paper_by_author/{author_filename.replace(' ', '%20')}"
                grouped_authors_markdown.append(f"[{author} ({count})]({author_link}) | ")

            # Join the Markdown content into a single string
            grouped_authors_markdown_str = "".join(grouped_authors_markdown).rstrip(" | ")

            # Save the sorted Markdown to a temporary file for the workflow
            write_file("update_template_or_data/author_grouping.md", grouped_authors_markdown_str)
        except Exception as e:
            logging.error(f"Error generating sorted author grouping Markdown: {str(e)}", exc_info=True)



        # Generate author-specific files
        try:
            # Count authors across papers
            author_counter = Counter()
            for _, row in papers_df.iterrows():
                authors = row['Authors']
                author_list = [author.strip() for author in authors.split(',')]
                author_counter.update(author_list)

            num_top_author = 20
            top_authors = [author for author, _ in author_counter.most_common(num_top_author)]

            # Create directory for author-specific grouping
            subgroup_dir = "paper_by_author"
            if not os.path.exists(subgroup_dir):
                os.makedirs(subgroup_dir)

            for author in top_authors:
                filtered_df = papers_df[papers_df['Authors'].str.contains(author, case=False, na=False)]
                if not filtered_df.empty:
                    sorted_markdown = []
                    for _, row in filtered_df.iterrows():
                        markdown_entry = f"- [{row['Title']}]({row['Link']})\n" \
                                         f"    - {row['Authors']}\n" \
                                         f"    - 🏛️ Institutions: {row['Institutions']}\n" \
                                         f"    - 📅 Date: {row['Original Date']}\n" \
                                         f"    - 📑 Publisher: {row['Publisher']}\n" \
                                         f"    - 💻 Env: {row['Env']}\n" \
                                         f"    - 🔑 Key: {row['Keywords']}\n" \
                                         f"    - 📖 TLDR: {row['TLDR']}\n"
                        sorted_markdown.append(markdown_entry)

                    author_filename = f"paper_{author.replace(' ', '_')}.md"
                    author_file_path = os.path.join(subgroup_dir, author_filename)
                    write_file(author_file_path, f"# {author}'s Papers\n\n" + "\n".join(sorted_markdown))
        except Exception as e:
            logging.error(f"Error generating author-specific files: {str(e)}", exc_info=True)

        # Generate environment-specific files
        try:
            subgroup_dir = "paper_by_env"
            if not os.path.exists(subgroup_dir):
                os.makedirs(subgroup_dir)

            env_keywords = {
                "Web": "paper_web.md",
                "Desktop": "paper_desktop.md",
                "Mobile": "paper_mobile.md",
                "GUI": "paper_gui.md",
                "Misc": "paper_misc.md"
            }

            for env_key, file_name in env_keywords.items():
                filtered_df = papers_df[papers_df['Env'].str.contains(env_key, case=False, na=False)]
                if not filtered_df.empty:
                    sorted_markdown = []
                    for _, row in filtered_df.iterrows():
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
                    file_path = os.path.join(subgroup_dir, file_name)
                    write_file(file_path, final_output)
        except Exception as e:
            logging.error(f"Error generating environment-specific files: {str(e)}", exc_info=True)

        subgroup_dir = "paper_by_key"
        if not os.path.exists(subgroup_dir):
            os.makedirs(subgroup_dir)

        for keyword in keywords_to_group:
            filtered_df = papers_df[papers_df['Keywords'].str.contains(keyword, case=False, na=False)]
            if not filtered_df.empty:
                sorted_markdown = []
                for _, row in filtered_df.iterrows():
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
                file_path = os.path.join(subgroup_dir, f"paper_{keyword}.md")
                write_file(file_path, f"# Papers with Keyword: {keyword}\n\n" + final_output)
    except Exception as e:
        logging.error(f"Error generating keyword-based Markdown files: {str(e)}", exc_info=True)

    # Generate sorted keyword grouping markdown
    # Generate sorted keyword grouping markdown with predefined keywords prioritized
    try:
        # Extract and count all keywords
        all_keywords = []
        for _, row in papers_df.iterrows():
            keywords = row['Keywords']
            filtered_keywords = [remove_square_brackets(kw.strip()) for kw in keywords.split(",") if kw.strip()]
            all_keywords.extend(filtered_keywords)
        keyword_counter = Counter(all_keywords)

        # Define predefined keywords
        predefined_keywords = ["Model", "Framework", "Benchmark", "Dataset",  "Safety", "Survey"]

        # Get counts for predefined keywords
        predefined_keyword_counts = [(kw, keyword_counter[kw]) for kw in predefined_keywords if kw in keyword_counter]

        # Find remaining top keywords excluding predefined ones
        remaining_keywords = [
            (kw, count) for kw, count in keyword_counter.most_common()
            if kw not in predefined_keywords
        ]

        # Limit to top (20 - predefined_keywords) remaining keywords
        top_num_keywords = 20 - len(predefined_keywords)
        top_remaining_keywords = remaining_keywords[:top_num_keywords]

        # Combine predefined and top remaining keywords
        combined_keywords = predefined_keyword_counts + top_remaining_keywords

        # Sort combined keywords by count in descending order (within their respective groups)
        combined_keywords.sort(
            key=lambda x: (-x[1], predefined_keywords.index(x[0]) if x[0] in predefined_keywords else float('inf')))

        # Generate Markdown content for keywords
        grouped_keywords_markdown = []
        for keyword, count in combined_keywords:
            keyword_filename = f"paper_{keyword.replace(' ', '_')}.md"
            keyword_link = f"paper_by_key/{keyword_filename.replace(' ', '%20')}"
            grouped_keywords_markdown.append(f"[{keyword} ({count})]({keyword_link}) | ")

        # Join the Markdown content into a single string
        grouped_keywords_markdown_str = "".join(grouped_keywords_markdown).rstrip(" | ")

        # Save the sorted Markdown to a temporary file for the workflow
        write_file("update_template_or_data/keyword_grouping.md", grouped_keywords_markdown_str)
    except Exception as e:
        logging.error(f"Error generating sorted keyword grouping Markdown: {str(e)}", exc_info=True)

    # Generate keyword word cloud
    try:


        all_keywords = []
        for _, row in papers_df.iterrows():
            keywords = row['Keywords']
            filtered_keywords = [remove_square_brackets(kw.strip()) for kw in keywords.split(",") if kw.strip()]
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

        wordcloud = WordCloud(
            width=2000, height=1000, background_color="white", max_font_size=140, min_font_size=10
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