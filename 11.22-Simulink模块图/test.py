import markdown
import requests
import os
import re

# 读取Markdown文件内容
with open('Simulink模块图.md', 'r', encoding='utf-8') as file:
    md_content = file.read()

# 解析Markdown内容
md = markdown.Markdown(extensions=['markdown.extensions.meta'])
html = md.convert(md_content)

# 查找所有的图片链接
img_urls = re.findall(r'!\[.*?\]\((.*?)\)', md_content)

# 创建保存图片的目录
img_dir = 'images'
os.makedirs(img_dir, exist_ok=True)

# 下载图片并保存到本地
for img_url in img_urls:
    img_name = os.path.basename(img_url)
    img_path = os.path.join(img_dir, img_name)
    
    # 下载图片
    response = requests.get(img_url)
    if response.status_code == 200:
        with open(img_path, 'wb') as img_file:
            img_file.write(response.content)
        print(f"Downloaded {img_url} to {img_path}")
    else:
        print(f"Failed to download {img_url}")

    # 替换Markdown文件中的图片链接
    md_content = md_content.replace(img_url, f'./{img_dir}/{img_name}')

# 将修改后的Markdown内容写回文件
with open('Simulink模块图_modified.md', 'w', encoding='utf-8') as file:
    file.write(md_content)

print("Markdown file has been updated with local image paths.")