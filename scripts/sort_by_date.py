# Parsing and ordering all paper entries based on the extracted file content

import pandas as pd
import calendar
import re


# 读取文件内容
paper_source="update_template_or_data/update_paper_list.md"
with open(paper_source, "r", encoding="utf-8") as file:
    sample_input = file.read()


def parse_date_with_defaults(date_str):
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


# Define regex pattern based on new input format
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

# Extract data and process it
parsed_entries = []
for match in new_format_pattern.findall(sample_input):
    title, link, authors, institutions, date, publisher, env, keywords, tldr = match
    parsed_date = parse_date_with_defaults(date)
    # Wrap keywords in brackets, split by commas
    formatted_keywords = ", ".join([f"{kw.strip()}" for kw in keywords.split(",")])
    parsed_entries.append((title, link, authors, institutions, date, parsed_date, publisher, f"[{env.strip()}]",
                           formatted_keywords, tldr))

# Convert to DataFrame and sort
papers_df = pd.DataFrame(parsed_entries, columns=[
    'Title', 'Link', 'Authors', 'Institutions', 'Original Date', 'Parsed Date', 'Publisher', 'Env', 'Keywords', 'TLDR'
]).drop_duplicates(subset='Title', keep='first')
papers_df.sort_values(by='Parsed Date', ascending=False, inplace=True)

# Format output to new specified Markdown structure
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

# Combine into final output
final_output = "\n".join(sorted_markdown)

# print((final_output))

print(papers_df)

with open("update_template_or_data/update_paper_list.md", "w", encoding="utf-8") as file:
    file.write(final_output)

import os

# 1. 创建子集的文件夹，如果没有的话
subgroup_dir = "update_template_or_data/tmp"
if not os.path.exists(subgroup_dir):
    os.makedirs(subgroup_dir)

# 2. 定义一个映射表，用于不同的env关键字
env_keywords = {
    "web": "env_web.md",
    "desktop": "env_desktop.md",
    "mobile": "env_mobile.md",
    "gui": "env_gui.md",
    "general": "env_general.md"
}

# 3. 根据env字段进行过滤并生成相应的Markdown文件
for env_key, file_name in env_keywords.items():
    filtered_df = papers_df[papers_df['Env'].str.contains(env_key, case=False, na=False)]

    # 4. 生成每个env子集合的Markdown
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

        # 5. 写入文件
        final_output = "\n".join(sorted_markdown)
        file_path = os.path.join(subgroup_dir, file_name)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(final_output)
        print(f"生成文件：{file_path}")

