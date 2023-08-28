import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 读取图片
img1 = cv.imread("./image/horse.jpg")
# 2.图像缩放
# 2.1 绝对尺寸
rows,cols = img1.shape[:2]
res = cv.resize(img1,(2*cols,2*rows),interpolation=cv.INTER_CUBIC) # interpolation：插值方法

# 2.2 相对尺寸
res1 = cv.resize(img1,None,fx=0.5,fy=0.5)

# 3 图像显示
# 3.1 使用opencv显示图像(不推荐)
cv.imshow("orignal",img1)
cv.imshow("enlarge",res)
cv.imshow("shrink）",res1)
cv.waitKey(0)

# 3.2 使用matplotlib显示图像
fig,axes=plt.subplots(nrows=1,ncols=3,figsize=(10,8),dpi=100)
# 将创建一个1行3列的图像，其中每个子图对象都可以通过axes[0]、axes[1]和axes[2]进行访问

axes[0].imshow(res[:,:,::-1])
axes[0].set_title("绝对尺度（放大）")
axes[1].imshow(img1[:,:,::-1])
axes[1].set_title("原图")
axes[2].imshow(res1[:,:,::-1])
axes[2].set_title("相对尺度（缩小）")
plt.show()