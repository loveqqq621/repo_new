
# import cv2

# # 创建一个视频捕捉对象
# cap = cv2.VideoCapture(video_path)

# # 检查视频是否成功打开
# if not cap.isOpened():
#     print("无法打开视频文件:", video_path)
#     exit()

# # 循环读取和显示视频帧
# while True:
#     # 逐帧读取视频
#     ret, frame = cap.read()

#     # 如果视频帧读取失败，则退出循环
#     if not ret:
#         break

#     # 在窗口中显示视频帧
#     cv2.imshow("Video", frame)

#     # 等待按下 'q' 键来退出循环
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # 释放资源
# cap.release()
# cv2.destroyAllWindows()




# import pygame
# from PIL import Image, ImageSequence

# # 初始化pygame
# pygame.init()

# # 设置窗口大小
# screen_width, screen_height = 800, 600
# screen = pygame.display.set_mode((screen_width, screen_height))

# # 加载视频文件

# video = Image.open(video_path)

# # 获取视频的帧数和帧率
# num_frames = video.n_frames
# fps = video.info['fps']

# # 循环播放视频
# frame_index = 0
# clock = pygame.time.Clock()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#     # 获取当前帧的图像并转换为pygame支持的图像格式
#     video.seek(frame_index)
#     frame = video.convert("RGB")
#     frame_surface = pygame.image.fromstring(frame.tobytes(), frame.size, "RGB")

#     # 在屏幕上绘制当前帧
#     screen.blit(frame_surface, (0, 0))

#     # 刷新屏幕
#     pygame.display.flip()

#     # 计算下一帧的索引
#     frame_index = (frame_index + 1) % num_frames

#     # 控制帧率
#     clock.tick(fps)


# import cv2
# import os

# # 设置视频文件路径和输出图像目录
# video_path = "images/opening.mp4"
# output_dir = "frames"

# # 创建输出图像目录
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# # 打开视频文件
# cap = cv2.VideoCapture(video_path)

# # 逐帧读取视频并保存为图像文件
# frame_index = 0
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     output_path = os.path.join(output_dir, f"frame{frame_index:04d}.jpg")
#     cv2.imwrite(output_path, frame)
#     frame_index += 1

# # 释放视频文件
# cap.release()







# # --------------------
# import pygame
# import cv2

# # --- local (built-in) camera ---
# #stream = 0

# # --- local file ---
# #stream = '2019-03-26_08-43-15.mkv'

# # --- http stream ---
# # doesn't work any more
# #stream = 'http://media.dumpert.nl/tablet/9f7c6290_Verstappen_vs._Rosberg_with_Horner_Smile___Streamable.mp4.mp4.mp4'

# # --- rtsp stream ---
# #stream = 'rtsp://streaming1.osu.edu/media2/ufsap/ufsap.mov'

# # --- rtmp stream ---
# # Big Buck Bunny
# stream = 'images/opening.mp4'

# # open stream
# cap = cv2.VideoCapture(stream)

# # read one frame and check if there was no problem
# ret, img = cap.read()
# if not ret:
#     print("Can't read stream")
#     #exit()

# # transpose/rotate frame 
# #img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# img = cv2.transpose(img)

# # display its width, height, color_depth
# print('shape:', img.shape)

# pygame.init()

# # create window with the same size as frame
# screen = pygame.display.set_mode((img.shape[0], img.shape[1]))

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#             # print('running false')

#     # read one frame and check if there was no problem
#     ret, img = cap.read()
#     if not ret:
#         running = False
#         break
#     else:
#         # transpose/rotate frame
#         #img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
#         #img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
#         img = cv2.transpose(img)

#         # blit directly on screen         
#         pygame.surfarray.blit_array(screen, img)

#     pygame.display.flip()
# cap.release()
# cv2.destroyAllWindows()
# # pygame.quit()



import pygame
import sys
import cv2
import numpy as np
import os
file_path = os.path.abspath(__file__)
file_path = os.path.dirname(file_path)
file_path = os.path.join(file_path, 'materials/')


pygame.init()  # 初始化pygame
FPS = 59.94
#设置窗口位置
os.environ["SDL_VIDEO_WINDOW_POS"]="%d,%d" % (50,70)
# FPSClock = pygame.time.Clock()
size = width, height = 800, 488  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
# pygame.display.set_caption(u"打字游戏:反应练习")
color = (255, 255, 255)  # 设置颜色

# ogg=pygame.mixer.Sound("game.ogg")
# pygame.mixer.music.load("")

pygame.init()
pygame.mixer.music.load(os.path.join(file_path, 'sounds/bgm.MP3'))
pygame.mixer.music.play()
videoCapture = cv2.VideoCapture(os.path.join(file_path, "images/end_v113.mp4"))
# cv2.namedWindow('name', )

while True:
    a=pygame.time.get_ticks()
    if videoCapture.isOpened():
        #从opncv读一段视频进来
        ret, frame = videoCapture.read()
        

        # cv2.namedWindow("test", 0)  
           # 设置窗口的长和宽
        # cv2.imshow('test', frame)
        #下面这句可以获取图像大小
        print("frame.shape:", frame.shape)
        # 
        # rot90(m, k=1, axes=(0, 1)
        # m是要旋转的数组(矩阵)，
        # k是旋转的次数，默认旋转1次，
        # 那是顺时针还是逆时针呢？
        # 正数表示逆时针，而k为负数时则是对数组进行顺时针方向的旋转。
        # 视频结束时会丢出一个ValueError异常
        try:
            # frame = np.rot90(frame,k=-1)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            # print(frame)
        except:
            continue
        if frame is not None:
            # print(frame)
            frame = cv2.resize(frame, (488, 800))
            frame = pygame.surfarray.make_surface(frame)

            frame=pygame.transform.flip(frame,False,True)
            

        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    
            screen.blit(frame, (0,0))
    else:
        break
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
    pygame.display.flip()  # 更新全部显示
    # time_next= FPSClock.tick(FPS)
    # b=pygame.time.get_ticks()
videoCapture.release()
cv2.destroyAllWindows()


