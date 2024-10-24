import os
from PIL import Image
from glob import glob


##删除小图片
def del_small_file(file_name):
    size = os.path.getsize(file_name)
    file_size = 10*1024
    if size < file_size:
        print('remove',size,file_name)
        os.remove(file_name)

##图片缩放到固定的宽度
def resize_files(file_path,_width = 800):
    try:
        print(f'图片resize处理中：{file_path}')
        im = Image.open(file_path)
        (x,y) = im.size #read image size
        x_s = _width #define standard width
        y_s = int(y * x_s / x) #calc height based on standard width
        out = im.resize((x_s,y_s),Image.LANCZOS) #resize image with high-quality
        out.save(file_path)
        
    except Exception as e:
        print('error:',e)
       
        # pass
        # 存在一些文件打不开，此处需要稍作清洗


if __name__=='__main__':
    # resize_files('./image_files',600)
##    delete_invalid_files()
    for item in glob('./*.png',recursive=False):
        print(item)
        resize_files(item,500)
