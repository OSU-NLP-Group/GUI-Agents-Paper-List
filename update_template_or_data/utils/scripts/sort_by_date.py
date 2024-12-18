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
subgroup_dir = "paper_by_env"
if not os.path.exists(subgroup_dir):
    os.makedirs(subgroup_dir)

# 2. 定义一个映射表，用于不同的env关键字
env_keywords = {
    "Web": "paper_web.md",
    "Desktop": "paper_desktop.md",
    "Mobile": "paper_mobile.md",
    "GUI": "paper_gui.md",
    "Misc": "paper_misc.md"
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
from collections import Counter
import os

# 1. 初始化一个Counter来统计作者作品数量
author_counter = Counter()

# 2. 遍历论文条目，统计每个作者的作品数量
for _, row in papers_df.iterrows():
    authors = row['Authors']
    author_list = [author.strip() for author in authors.split(',')]  # 假设作者以逗号分隔
    author_counter.update(author_list)

# 3. 获取作品最多的前15个作者
top_authors = [author for author, _ in author_counter.most_common(15)]

# 4. 为每个作者生成一个文件，只包含该作者的论文
subgroup_dir = "paper_by_author"
if not os.path.exists(subgroup_dir):
    os.makedirs(subgroup_dir)

for author in top_authors:
    # 筛选出包含该作者的论文
    author_papers_df = papers_df[papers_df['Authors'].str.contains(author, case=False, na=False)]

    # 生成每个作者的Markdown内容
    sorted_markdown = []
    for _, row in author_papers_df.iterrows():
        markdown_entry = f"- [{row['Title']}]({row['Link']})\n" \
                         f"    - {row['Authors']}\n" \
                         f"    - 🏛️ Institutions: {row['Institutions']}\n" \
                         f"    - 📅 Date: {row['Original Date']}\n" \
                         f"    - 📑 Publisher: {row['Publisher']}\n" \
                         f"    - 💻 Env: {row['Env']}\n" \
                         f"    - 🔑 Key: {row['Keywords']}\n" \
                         f"    - 📖 TLDR: {row['TLDR']}\n"
        sorted_markdown.append(markdown_entry)

    # 5. 保存文件
    author_filename = f"paper_{author.replace(' ', '_')}.md"
    author_file_path = os.path.join(subgroup_dir, author_filename)
    with open(author_file_path, "w", encoding="utf-8") as file:
        file.write(f"# {author}'s Papers\n\n")
        file.write("\n".join(sorted_markdown))

    print(f"生成文件：{author_file_path}")



import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
#
# 1. 初始化一个Counter来统计作者作品数量
author_counter = Counter()


num_top_author=10
# 2. 遍历论文条目，统计每个作者的作品数量
for _, row in papers_df.iterrows():
    authors = row['Authors']
    author_list = [author.strip() for author in authors.split(',')]  # 假设作者以逗号分隔
    author_counter.update(author_list)

# 3. 获取作品最多的前15个作者
top_authors = [author for author, _ in author_counter.most_common(num_top_author)]

# 4. 获取前15个作者的作品数量
top_15_counts = [author_counter[author] for author in top_authors]

# 5. 创建条形图
plt.figure(figsize=(10, 10))  # 设置图表大小
sns.barplot(x=top_15_counts, y=top_authors, palette="viridis")

# 6. 设置图表标题和标签
plt.title("Top Authors by Number of Papers", fontsize=20)
plt.xlabel("Number of Papers", fontsize=20)
plt.ylabel("Authors", fontsize=20)

# 7. 美化图表（可选）
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.tight_layout()

# 8. 保存图表到文件
plt.savefig("update_template_or_data/statistics/top_authors.png")

# 9. 显示图表
# plt.show()

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re
def remove_square_brackets(s):
    # 使用正则表达式去除开头和结尾的方括号
    return re.sub(r'^\[|\]$', '', s)
# 1. 定义排除的关键词
# excluded_keywords = {"[model]", "[framework]", "[benchmark]", "[dataset]"}


from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# 1. 定义排除的关键词
# excluded_keywords = {"model", "framework", "benchmark", "dataset"}
excluded_keywords = {}

# 2. 提取所有论文的关键词并计算频率（排除特定关键词）
# Remove any leading or trailing spaces, and split by commas if necessary
all_keywords = []
for _, row in papers_df.iterrows():
    keywords = row['Keywords']
    # Ensure keywords are split correctly and clean them
    filtered_keywords = [kw.strip() for kw in keywords.split(",") if kw.strip()]
    all_keywords.extend(filtered_keywords)

# Calculate the frequency of each keyword
keyword_counts = Counter(all_keywords)

print(keyword_counts)
wordcloud = WordCloud(
    width=1000,
    height=1000,
    background_color="white",
    colormap="viridis",
    contour_width=0,
    contour_color='black',
).generate_from_frequencies(keyword_counts)

# Reduce DPI for better scaling
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)

# Lower DPI to avoid large images
plt.savefig("update_template_or_data/statistics/keyword_wordcloud.png", format='png', dpi=460)  # Set lower DPI for smaller file size
plt.close()
