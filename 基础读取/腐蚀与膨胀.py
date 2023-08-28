"""
膨胀就是使图像中高亮部分扩张，效果图拥有比原图更大的高亮区域；
腐蚀是原图中的高亮区域被蚕食，效果图拥有比原图更小的高亮区域。
膨胀是求局部最大值的操作，腐蚀是求局部最小值的操作。
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1 读取图像
img = cv.imread("./image/letter.png")
# 2 创建核结构,即卷积的核结构，为一个二维数组
kernel = np.ones((5, 5), np.uint8)

# 3 图像腐蚀和膨胀
erosion = cv.erode(img, kernel) # 腐蚀
dilate = cv.dilate(img,kernel) # 膨胀

# 4 图像展示
fig,axes=plt.subplots(nrows=1,ncols=3,figsize=(10,8),dpi=100)
axes[0].imshow(img)
axes[0].set_title("原图")
axes[1].imshow(erosion)
axes[1].set_title("腐蚀后结果")
axes[2].imshow(dilate)
axes[2].set_title("膨胀后结果")
plt.show()