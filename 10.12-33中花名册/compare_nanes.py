import re

def read_file(file_path):
    """读取文件内容并返回一个集合"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(line.strip() for line in file)

def clean_names(names):
    """去掉名字中的除汉字以外的字符"""
    cleaned_names = set()
    for name in names:
        # 使用正则表达式去掉除汉字以外的字符
        cleaned_name = re.sub(r'[^\u4e00-\u9fa5]', '', name).strip()
        if cleaned_name:
            cleaned_names.add(cleaned_name)
    return cleaned_names

def compare_files(file1_path, file2_path):
    """比较两个文件的名单"""
    # 读取两个文件的内容
    names1 = read_file(file1_path)
    names2 = read_file(file2_path)

    # 去掉第二个文件中的除汉字以外的字符
    names2_cleaned = clean_names(names2)

    # 找出在第一个文件中但不在第二个文件中的名字
    only_in_file1 = names1 - names2_cleaned

    # 找出在第二个文件中但不在第一个文件中的名字
    only_in_file2 = names2_cleaned - names1

    return only_in_file1, only_in_file2

def print_results(only_in_file1, only_in_file2):
    """打印比较结果"""
    print("只在第一个文件中的名字:")
    for name in only_in_file1:
        print(name)

    print("\n只在第二个文件中的名字:")
    for name in only_in_file2:
        print(name)


# 文件路径
file1_path = '花名册.txt'
file2_path = '名单2.txt'

# 比较文件
only_in_file1, only_in_file2 = compare_files(file1_path, file2_path)

# 打印结果
print_results(only_in_file1, only_in_file2)


