import os
import cv2
# path = r'E:\python\图像处理\OpenCV_API\基础读取\image\num\num8.png'  # 图像所在路径
# filelist = os.listdir(path)
# print(len(filelist))
# for file in filelist:
#     orgin_dir = os.path.join(path, file) # 原路径
#     print(orgin_dir)  # 检查路径
#     img = cv2.imread(orgin_dir, cv2.IMREAD_GRAYSCALE)  # 读取灰度图
#     # print(img.shape)  # 打印维度
#     cv2.imwrite(orgin_dir, img)  # 覆盖原图

file_path = r"E:\img\opencv\num9.jpg"
img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
#
print(img.shape)
cv2.imwrite(file_path, img)

# opencv中进行通道转换需要将图片路径转换为全英文路径