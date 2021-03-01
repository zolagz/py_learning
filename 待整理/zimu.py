from moviepy.editor import *
from os.path import splitext, isfile

from moviepy.editor import (VideoFileClip,
                            TextClip,
                            CompositeVideoClip)
# 本地视频位置
from moviepy.video.VideoClip import TextClip

class RealizeAddSubtitles():
    '''
    合成字幕与视频
    '''
    def __init__(self, videoFile, txtFile):
        self.src_video = videoFile
        self.sentences = txtFile
        # src_video = input('请输入视频文件路径')
        # sentences = input('请输入字幕文件路径')
        if not (isfile(self.src_video) and self.src_video.endswith(('.avi', '.mp4')) and isfile(
                self.sentences) and self.sentences.endswith(
                '.txt')):
            print('视频仅支持avi以及mp4，字幕仅支持txt格式')
        else:
            video = VideoFileClip(self.src_video)
            # 获取视频的宽度和高度
            w, h = video.w, video.h
            # 所有字幕剪辑
            txts = []
            with open(self.sentences, encoding='utf-8') as fp:
                for line in fp:
                    sentences, start, span = line.split(':')
                    start, span = map(float, (start, span))
                    print(sentences)
                    print(start)
                    print(span)
                    print("="*20)
                    txt = (TextClip(txt=sentences,color='white',font='src/font/kaiti.ttf',bg_color='#8552a1',transparent=True,fontsize=35).set_position(('center',0.85), relative=True).set_duration(span).set_start(start))
                    # txt = (TextClip(sentences, fontsize=40,
                    #                 font='Amiri-Bold',bg_color='#8552a1',
                    #                 align='center', color='black').set_position((45,150)).set_duration(span).set_start(start))
                    txts.append(txt)
            # 合成视频，写入文件
            video = CompositeVideoClip([video] + txts,size=(1280, 720))
            # cvc = CompositeVideoClip([video] + result_list, size=(1280, 720))

            fn, ext = splitext(self.src_video)
            video.write_videofile(f'{fn}_带字幕{ext}')

# txt_clip = TextClip("Just from test, title 2021",color='white',font='Amiri-Bold',bg_color='#8552a1',transparent=True,fontsize=100).set_position((45,150)).set_duration(video.duration)
# result = CompositeVideoClip([video, txt_clip])  # 在视频上覆盖文本

if __name__ == '__main__':
    RealizeAddSubtitles('src/001.mp4','src/text.txt')