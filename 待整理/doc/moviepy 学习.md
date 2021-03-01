###使用moviepy如何剪辑视频：

[原文链接](https://zhuanlan.zhihu.com/p/138984453)


```
from moviepy.editor import *
# 剪切视屏bws.mp4中第50秒到第60秒
clip = VideoFileClip('bws.mp4').subclip(50, 60)
# 将剪切的片段保存
clip.write_videofile("clip.mp4")

```
####1、提取音频文件

在VideoFileClip类中，音频文件作为其中的一个参数，我们可以直接获取：

```
from moviepy.editor import *
# 读取视频文件
video = VideoFileClip('bws.mp4')
# 获取其中音频
audio = video.audio
# 保存音频文件
audio.write_audiofile('audio.mp3')

```

#####2、混流

我们还可以将音频同视频混流，在moviepy中，提供了一个读取音频文件的类，我们设置视频的音频需要创建这个类的对象：

```
from moviepy.editor import *
# 读取视频
video = VideoFileClip('bws.mp4')
# 读取音频
audio = AudioFileClip('百年孤独.mp3')
# 设置视频的音频
video = video.set_audio(audio)
# 保存新的视频文件
video.write_videofile('bws_audio.mp4')

```

#### 3、逐帧提取画面

我们都知道，视频是由一帧一帧的图片组成的，我们也可以将画面一帧一帧提取出来：

```
import cv2
# 读取视频
video = cv2.VideoCapture('bws.mp4')
# 逐帧读取，当还有画面时ret为True，frame为当前帧的ndarray对象
ret, frame = video.read()
i = 0
# 循环读取
while ret:
    i += 1
    cv2.imwrite('v'+str(i) + '.jpg', frame)
    ret, frame = video.read()

```
上述代码就能将视屏的每一帧以图片的形式保存下来。

#### 4、截取gif

截取gif和截取视频没有什么区别，不过为了减少gif的大小，我们通常会对视频进行尺寸缩放：

```
from moviepy.editor import *
# 读取视频
video = VideoFileClip('bws.mp4')
# 裁剪视频，并缩小一半
video = video.subclip(20, 30).resize((0.5))
# 保存gif图片
video.write_gif('bws.gif')

在上面subclip方法中，我们可以传入元组，例如：

video.subclip((1, 20), (2, 30))
```

其含义为从1分20秒截取到2分30秒。


-----

[Python视频处理案例六则：旋转视频、调整音量/播放速度、淡入淡出、插入转场素材 ](https://www.sohu.com/a/337829735_797291)

#### 5 淡入淡出并插入转场图片 

```


from moviepy.editor import *
video = VideoFileClip('001.mp4')
video1 = video.subclip(0,5).fadein(3,(1,1,1)).fadeout(2,(1,1,1))

video2 = video.subclip(6,10).fadein(3,(1,1,1)).fadeout(2,(1,1,1))

video3 = video.subclip(11,15).fadein(3,(1,1,1)).fadeout(2,(0,0,0))

transition = ImageClip('logo.png',duration=2).resize(video.size)

resultVideo = concatenate_videoclips([video1,video2,video3],transition=transition)

resultVideo.write_videofile("tr_clip.mp4")


```

#### 淡入淡出并插入转场视频 

```
from moviepy.editor import *
video = VideoFileClip('001.mp4')
video1 = video.subclip(0,5).fadein(3,(1,1,1)).fadeout(2,(1,1,1))

video2 = video.subclip(6,10).fadein(3,(1,1,1)).fadeout(2,(1,1,1))

video3 = video.subclip(11,15).fadein(3,(1,1,1)).fadeout(2,(0,0,0))

transition = VideoFileClip('001.mp4').subclip(10,12).resize(video.size)

resultVideo = concatenate_videoclips([video1,transition,video2,transition,video3])

resultVideo.write_videofile("tr_clip.mp4")

```


图片转视频：

图片需要大小一致

```
import moviepy.video.io.ImageSequenceClip
import os

image_folder='src/frames'#open the image location
fps=29

image_files = [image_folder+'/'+img for img in os.listdir(image_folder) if img.endswith(".jpg")]
image_files.sort()
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('Movie1.mp4')

```

```

# 将图片按照顺序逐一放入movei模板中
def AddImageInBase(img_path,mp3_duration,title):
    # 判断如果没有该数据的文件夹就创建
    start_time = 0
    image_list = []

    images = os.listdir(img_path)  # os.listdir()方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    images.remove('.DS_Store')
    images.sort()

    for num in range(len(images)):
        # 获取该字段字符串

        # 每段字幕时长
        every_part_duration_time = mp3_duration / len(images)
    #     # 图片数据
        jpg_path = img_path + "/" + images[num]
        image_clip = (
            ImageClip(jpg_path)
                .set_duration(every_part_duration_time)  # 水印持续时间
                .resize(height=650)  # 水印的高度，会等比缩放
                .set_pos(("center", 0))  # 水印的位置
                .set_start(start_time)
        )
        start_time = start_time + every_part_duration_time
        image_list.append(image_clip)

    cvc = CompositeVideoClip(image_list, size=(1280, 720))
    cvc.write_videofile("src/jpg.mp4", fps=24, remove_temp=False, verbose=True)
    print('视频合成完成')


# mp3_duration = librosa.get_duration(filename='src/1302.mp3')

# print(mp3_duration)
AddImageInBase('src/img',30,'just for test 01 ')

```


