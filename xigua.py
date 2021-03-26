import requests

import os
import re, json
import base64

# url = "https://www.ixigua.com/6896685054102077955?wid_try=1"
url = "https://www.ixigua.com/6902227057007133197?wid_try=1"

header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    # "sec-ch-ua": 'Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87'
}

main_page = requests.get(url, headers=header)
main_page.encoding = main_page.apparent_encoding
print(main_page.text)

re_str = "window._SSR_HYDRATED_DATA=(.*?)</script>"
json_data: str = re.compile(re_str).findall(main_page.text)[0]
# 转成 json 异常， 替换一下字符
replace = json_data.replace(":undefined", ':"undefined"').replace("null", '"null"')
print(replace)
json_loads = json.loads(replace)
print(json_loads)

paly_base64_url_ = \
    json_loads['anyVideo']['gidInformation']['packerData']['video']['videoResource']['dash']['dynamic_video'][
        'dynamic_video_list'][-1]['main_url']
audio_base64_url_ = \
    json_loads['anyVideo']['gidInformation']['packerData']['video']['videoResource']['dash']['dynamic_video'][
        'dynamic_audio_list'][-1]['main_url']
title = json_loads['anyVideo']['gidInformation']['packerData']['video']['title']
# 解密
play_url = base64.b64decode(paly_base64_url_).decode("utf-8")
audio_url = base64.b64decode(audio_base64_url_).decode("utf-8")

print("title", title)
print("play_url", play_url)
print("audio_url", audio_url)

video = requests.get(url=audio_url, headers=header)
with open(title + "audio.mp4", 'wb')as file:
    file.write(video.content)
    file.close()
    print("===>音频下载完成！")

video_file = requests.get(url=play_url, headers=header)
with open(title + "video.mp4", 'wb')as file:
    file.write(video_file.content)
    file.close()
    print("===>视频下载完成！")



