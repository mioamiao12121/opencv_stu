"""
图像直方图（Image Histogram）是用以表示数字图像中亮度分布的直方图，
标绘了图像中每个亮度值的像素个数。
横坐标的左侧为较暗的区域，而右侧为较亮的区域
因此一张较暗图片的直方图中的数据多集中于左侧和中间部分，而整体明亮、只有少量阴影的图像则相反。
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# 1 直接以灰度图的方式读入
img = cv.imread('./image/cat.jpeg',0)
# 2 统计灰度图
histr = cv.calcHist([img],[0],None,[256],[0,256])
# 3 绘制灰度图
plt.figure(figsize=(10,6),dpi=100)
plt.plot(histr)
plt.grid()
plt.show()