import cv2
from cv2 import VideoCapture

if __name__ == '__main__':
    cap = cv2.VideoCapture('./image/DOG.wmv')

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取视频的宽度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取视频的高度
    fps = cap.get(cv2.CAP_PROP_FPS)  # 获取视频的帧率
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))  # 视频的编码

    # 保存视频
    # 参数：（保存路径，编码器，帧率，画面尺寸，是否彩色）
    out = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height), True)

    while cap.isOpened():
        # 读取视频帧
        ret, frame = cap.read()
        if ret:
            # 边缘检测
            # 参数：（输入图像，min梯度阈值，max梯度阈值，卷积核大小(default:3),梯度方程(default:False)）
            edges = cv2.Canny(frame, 100, 200)
            # 保存视频帧到视频容器
            out.write(edges)

            # 显示视频帧图片
            cv2.imshow('frame', edges)
            # 每帧的显示时间，并监听键盘事件
            key = cv2.waitKey(1)
            # 监听退出Q
            if key & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()