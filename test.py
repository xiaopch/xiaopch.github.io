import os
import glob

# 设置你的目录路径
directory_path = '《阿西莫夫中短篇科幻作品集》'

# 遍历目录中的所有.md文件
for md_file in glob.glob(os.path.join(directory_path, '*.md')):
    with open(md_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 处理每一行，确保每行末尾都有换行符，但标题后不添加<br>
    new_lines = []
    for line in lines:
        # 检查是否为标题行（简单的检查，可能需要根据实际情况调整）
        if line.strip().startswith('#'):
            new_lines.append(line)  # 标题行，直接添加
        else:
            # 非标题行，确保以<br>结束
            if not line.strip().endswith('<br>'):
                line += '<br>'
            new_lines.append(line)

    # 将修改后的内容写回文件
    with open(md_file, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

print("所有Markdown文件已更新。")