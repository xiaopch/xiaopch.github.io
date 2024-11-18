import os
import glob

# 设置你的目录路径
directory_path = '《阿西莫夫中短篇科幻作品集》'

# 遍历目录中的所有.md文件
for md_file in glob.glob(os.path.join(directory_path, '*.md')):
    with open(md_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 处理每一行，确保每行末尾都有换行符
    new_lines = [line + '\n' if not line.endswith('\n') else line for line in lines]

    # 将修改后的内容写回文件
    with open(md_file, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

print("所有Markdown文件已更新。")