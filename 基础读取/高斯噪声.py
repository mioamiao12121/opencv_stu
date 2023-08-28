import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 1 图像读取
img = cv.imread('./image/dogGasuss.jpeg')

# 2 高斯滤波cv2.GaussianBlur(src,ksize,sigmaX,sigmay,borderType)
# 参数：
# src: 输入图像
# ksize:高斯卷积核的大小，注意 ： 卷积核的宽度和高度都应为奇数，且可以不同
# sigmaX: 水平方向的标准差
# sigmaY: 垂直方向的标准差，默认值为0，表示与sigmaX相同
# borderType:填充边界类型
blur = cv.GaussianBlur(img,(3,3),1)


# 3 图像显示
plt.figure(figsize=(10,8),dpi=100)
plt.subplot(121),plt.imshow(img[:,:,::-1]),plt.title('原图')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur[:,:,::-1]),plt.title('高斯滤波后结果')
plt.xticks([]), plt.yticks([])
plt.show()