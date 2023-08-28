"""
Shi-Tomasi算法是对Harris角点检测算法的改进，一般会比Harris算法得到更好的角点。
Harris 算法的角点响应函数是将矩阵 M 的行列式值与 M 的迹相减，利用差值判断是否为角点。
后来Shi 和Tomasi 提出改进的方法是，若矩阵M的两个特征值中较小的一个大于阈值，则认为他是角点
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 1 读取图像
img = cv.imread('./image/tv.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) # 将彩色图像转换为灰度图像
# 2 角点检测
corners = cv.goodFeaturesToTrack(gray,1000,0.01,10)

# 3 绘制角点
for i in corners:
    x,y = i.ravel()
    cv.circle(img,(int(x),int(y)),2,(0,0,255),1)
# 4 图像展示
plt.figure(figsize=(10,8),dpi=100)
plt.imshow(img[:,:,::-1]),plt.title('shi-tomasi角点检测')
plt.xticks([]), plt.yticks([])
plt.show()