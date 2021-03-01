from moviepy.editor import *
# 读取视频
video = VideoFileClip('src/001.mp4')
# 读取音频
audio = AudioFileClip('src/007.mp3')
# 设置视频的音频
video = video.set_audio(audio)
# 保存新的视频文件
video.write_videofile('src/bws_audio.mp4')