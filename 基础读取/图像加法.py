import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1 读取图像 图像相加必须使得相加的两个图像的大小一致，图像加法应该图像的大小一致
img1 = cv.imread("./image/rain.jpg")
img2 = cv.imread("./image/view.jpg")

# 2 加法操作
img3 = cv.add(img1,img2) # cv中的加法
img4 = img1+img2 # 直接相加

# 3 图像显示
fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes[0].imshow(img3[:,:,::-1])
axes[0].set_title("cv中的加法")
axes[1].imshow(img4[:,:,::-1])
axes[1].set_title("直接相加")
plt.show()

# 图像按照权重进行混合
img3 = cv.addWeighted(img1,0.7,img2,0.3,0)
plt.figure(figsize=(8,8))
plt.imshow(img3[:,:,::-1])
plt.show()