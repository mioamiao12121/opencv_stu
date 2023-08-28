import numpy as np
import cv2
from multiprocessing import Process, Value
import time, os


def webcam_video(camera_number, cout):  # cout是python多进程里，多个进程共享的值常用方法

    cap = cv2.VideoCapture(camera_number)

    if (cap.isOpened() == False):
        print("Error opening video stream or file")
    # 保存视频的分辨率、帧数、格式设置
    frame_width = 1280
    frame_height = 960
    cap.set(3, frame_width)
    cap.set(4, frame_height)  # 定分辨率
    cap.set(cv2.CAP_PROP_FPS, 30)  # 定帧率
    out_file_name = os.path.join('E:/videos_1/', 'video_' + str(camera_number), 'video_m5.mp4')  # 输出路径
    # cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G')) avi
    out = cv2.VideoWriter(out_file_name, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30,
                          (frame_width, frame_height))  # mp4

    print('按q退出，按w保存,按e退出保存')
    while (True):
        # cap.read()按帧读取视频，ret,frame是获cap.read()方法的两个返回值。
        # 其中ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。frame就是每一帧的图像，是个三维矩阵。
        ret, frame = cap.read()
        if ret == True:

            cv2.imshow('camera_' + str(camera_number), frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if cv2.waitKey(1) & 0xFF == ord('w'):  # 按W开启保存模式
                cout.value = 1
                print('开始保存')
            if cv2.waitKey(1) & 0xFF == ord('e'):  # 按e退出保存
                cout.value = 0
                print('结束保存')
            if cout.value == 1:
                out.write(frame)
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # path1 = 'D:/video2/videos/1.mp4'
    # path2 = 'D:/video2/videos/2.mp4'
    cout = Value('i', 0)  # 打开一个值共享，目的是按一次键两个进程同时开始保存视频
    p1 = Process(target=webcam_video, args=(0, cout))
    p2 = Process(target=webcam_video, args=(1, cout))
    # p1= Thread(target = local_video,args=(path1,))
    # p2= Thread(target = local_video,args=(path2,))
    p1.start()
    step1 = time.time()  # 检测时间用的不重要
    p2.start()
    step2 = time.time()
    p1.join()
    o_step1 = time.time()
    print(o_step1 - step1)
    # p2.join()
    o_step2 = time.time()
    print(o_step2 - step2)

