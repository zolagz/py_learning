使用FFmpeg将字幕文件集成到视频文件

[添加字幕](https://blog.csdn.net/weixin_34224941/article/details/92087759)

字幕文件转换

字幕文件有很多种，常见的有 .srt , .ass 文件等,下面使用FFmpeg进行相互转换。

将.srt文件转换成.ass文件


    

ffmpeg -i subtitle.srt subtitle.ass

将.ass文件转换成.srt文件


    

ffmpeg -i subtitle.ass subtitle.srt

集成字幕，选择播放

这种字幕集成比较简单，播放时需要在播放器中选择相应的字幕文件。


    

ffmpeg -i input.mp4 -i subtitles.srt -c:s mov_text -c:v copy -c:a copy output.mp4

嵌入SRT字幕到视频文件
单独SRT字幕

字幕文件为subtitle.srt


    

ffmpeg -i video.avi -vf subtitles=subtitle.srt out.avi

嵌入在MKV等容器的字幕

将video.mkv中的字幕（默认）嵌入到out.avi文件


    

ffmpeg -i video.mkv -vf subtitles=video.mkv out.avi

将video.mkv中的字幕（第二个）嵌入到out.avi文件


    

ffmpeg -i video.mkv -vf subtitles=video.mkv:si out.avi

嵌入ASS字幕到视频文件


    

ffmpeg -i video.avi -vf "ass=subtitle.ass" out.avi