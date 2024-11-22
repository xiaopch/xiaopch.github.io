import html2text

def html_to_markdown(html_file, markdown_file):
    # 读取 HTML 文件内容
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # 创建 html2text 转换器
    h = html2text.HTML2Text()
    h.ignore_links = False  # 是否忽略链接
    h.ignore_images = False  # 是否忽略图片

    # 将 HTML 转换为 Markdown
    markdown_content = h.handle(html_content)

    # 将 Markdown 内容写入文件
    with open(markdown_file, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

if __name__ == "__main__":
    html_file = "index.html"  # 输入的 HTML 文件
    markdown_file = "output.md"  # 输出的 Markdown 文件
    html_to_markdown(html_file, markdown_file)
    print(f"HTML 文件已成功转换为 Markdown 文件: {markdown_file}")