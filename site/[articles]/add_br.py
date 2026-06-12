import os
import glob

def add_br_to_md_files(folder_path=".", skip_empty_lines=True):
    """
    读取文件夹下所有.md文件
    1. 先删除文件中所有的<br>
    2. 在非标题、非空行的行末添加<br>
    
    Args:
        folder_path: 文件夹路径，默认为当前文件夹
        skip_empty_lines: 是否跳过空行，默认为True
    """
    # 获取所有.md文件
    md_files = glob.glob(os.path.join(folder_path, "*.md"))
    
    if not md_files:
        print(f"在 {os.path.abspath(folder_path)} 中没有找到.md文件")
        return
    
    print(f"找到 {len(md_files)} 个.md文件")
    
    for file_path in md_files:
        print(f"正在处理: {os.path.basename(file_path)}")
        
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 第一步：删除所有已有的<br>标签（包括<br/>、<br />等各种格式）
        import re
        # 删除各种形式的<br>标签
        content = re.sub(r'<br\s*/?>', '', content)
        
        # 按行分割
        lines = content.splitlines(keepends=True)
        
        # 第二步：处理每一行，重新添加<br>
        new_lines = []
        for line in lines:
            # 去除行尾换行符
            line_content = line.rstrip('\n\r')
            has_newline = line.endswith('\n')
            
            # 判断是否为空行
            is_empty_line = line_content.strip() == ''
            
            # 跳过空行（保留原格式但不加<br>）
            if skip_empty_lines and is_empty_line:
                new_lines.append(line)
                continue
            
            # 判断是否为标题行（以#开头）
            is_heading = line_content.lstrip().startswith('#')
            
            if is_heading:
                # 标题行不加<br>
                new_lines.append(line_content + ('\n' if has_newline else ''))
            else:
                # 普通行添加<br>
                new_lines.append(line_content + '<br>' + ('\n' if has_newline else ''))
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)
        
        print(f"  ✓ 完成处理")
    
    print(f"\n所有文件处理完成！")

# 直接运行，处理当前文件夹
if __name__ == "__main__":
    add_br_to_md_files()