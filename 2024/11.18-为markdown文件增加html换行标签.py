import os
import glob

# 设置你的目录路径
directory_path = '《刘慈欣短篇科幻小说合集》'


# 遍历目录中的所有.md文件
for md_file in glob.glob(os.path.join(directory_path, '*.md')):
    with open(md_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 处理每一行，确保非空白行末尾都有换行符，但标题后不添加<br>
    new_lines = []
    in_code_block = False  # 用于标记是否处于代码块中

    for line in lines:
        # 检查是否进入或退出代码块
        if line.strip().startswith('```') or line.strip().endswith('```'):
            in_code_block = not in_code_block

        # 跳过空白行
        if not line.strip():
            new_lines.append(line)  # 保留空白行
            continue

        # 检查是否为标题行（简单的检查，可能需要根据实际情况调整）
        if line.strip().startswith('#'):
            new_lines.append(line)  # 标题行，直接添加
        elif in_code_block:  # 如果在代码块中，则不添加<br>
            new_lines.append(line)
        else:
            # 非标题行且不在代码块中，确保以<br>结束
            if not line.strip().endswith('<br>'):
                line += '<br>'
            new_lines.append(line)

    # 将修改后的内容写回文件
    with open(md_file, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

print("所有Markdown文件已更新。")