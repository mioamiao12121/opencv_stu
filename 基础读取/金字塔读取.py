import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 金字塔的底部是待处理图像的高分辨率表示，而顶部是低分辨率的近似，
# 层级越高，图像越小，分辨率越低。
# 1 图像读取
img = cv.imread("./image/rain.jpg")
# 2 进行图像采样
up_img = cv.pyrUp(img)  # 上采样操作
img_1 = cv.pyrDown(img)  # 下采样操作
# 3 图像显示
cv.imshow('enlarge', up_img)
cv.imshow('original', img)
cv.imshow('shrink', img_1)
cv.waitKey(0)
cv.destroyAllWindows()