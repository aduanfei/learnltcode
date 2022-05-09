import collections
import requests
from bs4 import BeautifulSoup

def get_calendar():
    url="https://www.maigoo.com/goomai/192653.html"
    res=requests.get(url)
    content=BeautifulSoup(res.content,"lxml")
    imgs=content.find_all(class_="cs")
    i=1
    for im in imgs:
        img=im.find("img")
        #print(img)
        src=img["src"]
        imgsrc=requests.get(src).content
        with open(str(i)+"月.jpg","wb") as f:
           f.write(imgsrc)
        i=i+1
        print(src)


import os

import PIL.Image as Image

IMAGES_PATH = r'E:\learnltcode\image\\'  # 图片集地址
IMAGES_FORMAT = ['.jpg', '.JPG']  # 图片格式
IMAGE_SIZE = 4096  # 每张小图片的大小
IMAGE_ROW = 12  # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 1  # 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_SAVE_PATH = r'E:\learnltcode\final.jpg'  # 图片转换后的地址

# 获取图片集地址下的所有图片名称
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
               os.path.splitext(name)[1] == item]
#image_names=['1月.jpg', '2月.jpg', '3月.jpg', '4月.jpg', '5月.jpg', '6月.jpg', '7月.jpg', '8月.jpg', '9月.jpg','10月.jpg', '11月.jpg', '12月.jpg']
#image_names.sort()
print("image_names", image_names)
# 简单的对于参数的设定和实际图片集的大小进行数量判断
if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
    raise ValueError("合成图片的参数和要求的数量不能匹配！")


# 定义图像拼接函数
def image_compose():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE))  # 创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
    return to_image.save(IMAGE_SAVE_PATH)  # 保存新图


image_compose()  # 调用函数
