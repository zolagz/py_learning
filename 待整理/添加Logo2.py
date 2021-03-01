import moviepy.editor as mp

# 视频
video = mp.VideoFileClip("001.mp4")

# 水印
logo = (mp.ImageClip("logo.png")
        # 水印持续时间
        .set_duration(video.duration)
        # 水印高度，等比缩放
        .resize(height=300)
        # 水印的位置
        .set_pos(('left', 'top')))

output = mp.CompositeVideoClip([video, logo])
# 加上aac才有声音
output.write_videofile("5_sec.mp42.mp4", audio_codec="aac", codec="libx264")