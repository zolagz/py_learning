import os
import cv2
from PIL import Image
import imageio


def jpg_to_video(framepath, path, fps):
    """ 将图片合成视频. path: 视频路径，fps: 帧率 """
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")

    images = os.listdir(framepath)  # os.listdir()方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    images.remove('.DS_Store')
    images.sort()
    image = Image.open(framepath + '/' + images[0])
    vw = cv2.VideoWriter(path, fourcc, fps, image.size)

    for img in images:
        # Image.open(str(image)+'.jpg').convert("RGB").save(str(image)+'.jpg')
        try:
            new_frame = cv2.imread(framepath + '/' + img)
            vw.write(new_frame)
        except Exception as exc:
            print(img, exc)
    vw.release()
    print(path, 'Synthetic success!')


if __name__ == '__main__':
    # PATH_TO_MOVIES = os.path.join('test_movies', 'beautiful_mind2.mp4')
    frame_path = 'frames'
    video_path = '2255landing.avi'

    # unlock_movie(PATH_TO_MOVIES)  # 视频转图片
    jpg_to_video(frame_path, video_path, 40)  # 图片转视频