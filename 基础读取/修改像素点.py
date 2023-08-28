import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# region 获取并修改某个点的像素点
img = cv.imread("./image/horse.jpg")
# 获取某个像素点的值
px = img[100,100]
print(px)
# 仅获取蓝色通道的强度值
blue = img[100,100,0]
print(blue)
# 修改某个位置的像素值
img[100,100] = [255,255,255]
xg=img[100,100]
print(xg)
# endregion