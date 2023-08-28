import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

large_image = cv.imread("./image/star.jpeg")
small_image = cv.imread("./image/sun.jpg")

# 将小图片匹配到大图片中
result = cv.matchTemplate(large_image, small_image, cv.TM_CCOEFF_NORMED)

# 获取匹配结果中最大值的位置（即最佳匹配位置）
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

# 获取小图片的宽度和高度
small_image_width = small_image.shape[1]
small_image_height = small_image.shape[0]

# 在大图片中绘制矩形框标记匹配位置
top_left = max_loc
bottom_right = (top_left[0] + small_image_width, top_left[1] + small_image_height)
cv.rectangle(large_image, top_left, bottom_right, (0, 255, 0), 2)

# 显示大图片及标记结果
cv.imshow("Result", large_image)
cv.waitKey(0)
cv.destroyAllWindows()
