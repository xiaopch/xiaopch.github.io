from PIL import Image

def create_thumbnail(input_path, output_path, size=(300, 200)):
    """
    创建图片的缩略图。

    :param input_path: 原始图片的路径
    :param output_path: 缩略图保存的路径
    :param size: 缩略图的大小，格式为(width, height)
    """
    # 打开图片
    with Image.open(input_path) as img:
        # 生成缩略图
        img.thumbnail(size)
        
        # 保存缩略图
        img.save(output_path)

# 使用示例
input_image_path = '5.jpg'  # 替换为你的图片路径
output_thumbnail_path = '5_thumbnail.jpg'  # 替换为你想保存缩略图的路径
create_thumbnail(input_image_path, output_thumbnail_path)