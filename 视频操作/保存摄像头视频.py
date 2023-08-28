import cv2

# 视频的本质上就是由一幅一幅的图片组成
# 24帧 60帧(表示一秒显示60张图片)


# 创建一个窗口
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 480)

# 打开摄像头
cap = cv2.VideoCapture(0)
# 打开视频
# cap = cv2.VideoCapture('1.mp4')
# 保存视频
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
vw = cv2.VideoWriter('123.mp4', fourcc, 30, (640, 480))

# 循环读取摄像头的每一帧
while True:
    # 读一帧数据，返回标记，True表示读到了数据，False表示没读到数据
    ret, frame = cap.read()

    # 可以根据ret做个判断
    if not ret:
        # 没读到数据，直接退出
        break
    vw.write(frame)
    #     显示数据
    cv2.imshow('video', frame)

    key = cv2.waitKey(1000 // 30)
    if key & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
vw.release()
cv2.destroyAllWindows()

