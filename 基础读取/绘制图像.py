import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1 创建一个空白的图像
img = np.ones((512,512,3), np.uint8)*255 # 纯白
img = np.zeros((512,512,3), np.uint8) # 纯黑
# 2 绘制图形
cv.line(img,(0,0),(511,511),(255,0,0),5) # 直线
cv.rectangle(img,(384,0),(510,128),(0,255,0),3) # 矩形：图像，左上角、右下角、颜色、线条宽度
cv.circle(img,(447,63), 63, (0,0,255), 6) # 圆形

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA) # 添加文字

# 3 图像展示
# plt.imshow(img[:,:,::-1])  # -1表示图像通道翻转
# plt.title('匹配结果'), plt.xticks([]), plt.yticks([])
# plt.show()
cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()