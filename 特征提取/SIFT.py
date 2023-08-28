"""
SIFT算法的实质是在不同的尺度空间上查找关键点(特征点)，并计算出关键点的方向。
SIFT所查找到的关键点是一些十分突出，不会因光照，仿射变换和噪音等因素而变化的点，
如角点、边缘点、暗区的亮点及亮区的暗点等。

SURF 算法，是SIFT算法的增强版，
它的计算量小，运算速度快，提取的特征与SIFT几乎相同，
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1 读取图像
img = cv.imread('./image/tv.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY) # 进行关键点检测图像，且为灰度图像， cv.COLOR_BGR2GRAY将彩色图像转换为单通道的灰度图

# 2 sift关键点检测
# 2.1 实例化sift对象
sift = cv.SIFT_create()

# 2.2 关键点检测：kp关键点信息包括方向，尺度，位置信息，des是关键点的描述符
kp,des=sift.detectAndCompute(gray,None)
# 2.3 在图像上绘制关键点的检测结果
cv.drawKeypoints(img,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# 3 图像显示
plt.figure(figsize=(8,6),dpi=100)
plt.imshow(img[:,:,::-1]),plt.title('sift检测')
plt.xticks([]), plt.yticks([])
plt.show()