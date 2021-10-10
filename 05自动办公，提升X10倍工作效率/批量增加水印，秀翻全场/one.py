# -*- coding: utf-8 -*-
import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont
import os


def process_file(file_path, output_dir):
    img = cv2.imread(file_path)
    if (isinstance(img, numpy.ndarray)):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    # 字体的格式
    textSize = 50
    # MAC 系统的 font_path 替换为'/System/Library/Fonts/PingFang.ttc'
    fontStyle = ImageFont.truetype(
        "C:\Windows\Fonts\STZHONGS.ttf", textSize, encoding="utf-8")
    # 绘制文本
    left = 100
    top = 100
    text = '文字水印'
    textColor = (168, 121, 103)
    draw.text((left, top), text, textColor, font=fontStyle)
    # 转换回OpenCV类型
    img2 = cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)
    # 保存图片
    file_name = file_path.split("/")[-1]
    cv2.imwrite(os.path.join(output_dir, file_name), img2)
    print(f"proceed {file_path}")


root, dirs, files = next(os.walk("tips_3/"))
for item in files:
    file_path = os.path.join(root, item)
    process_file(file_path, "tips_3_watermark")
