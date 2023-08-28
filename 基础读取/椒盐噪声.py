import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 1 图像读取
img = cv.imread('./image/dogsp.jpeg')


# 2 均值滤波cv.blur(src, ksize, anchor, borderType)
# 参数:
# src：输入图像
# ksize：卷积核的大小
# anchor：默认值 (-1,-1) ，表示核中心
# borderType：边界类型
blur = cv.blur(img,(5,5))

# 3 图像显示
plt.figure(figsize=(10,8),dpi=100)
plt.subplot(121),plt.imshow(img[:,:,::-1]),plt.title('原图')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur[:,:,::-1]),plt.title('均值滤波后结果')
plt.xticks([]), plt.yticks([])
plt.show()