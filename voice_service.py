# -*- coding: utf-8 -*-
from base64 import b64decode
import json
import configparser
from uuid import uuid4
from tencentcloud.common import credential
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tts.v20190823 import tts_client, models

"""

@Time           2021/3/21 3:36 下午
@Auther         guan
@Emai           guan.afred@gmail.com
@File           002.py
@Project        video_eidt

https://cloud.tencent.com/document/product/1073
https://cloud.tencent.com/document/product/1073/37995




"""


voice_id=1001



conf = configparser.ConfigParser()

conf.read("./conf/tcloud_auth.ini", encoding="UTF-8")
APPID = conf.getint("node1", "AppId")
SecretId = conf.get("node1", "SecretId")
SecretKey = conf.get("node1", "SecretKey")


user_text = '您好，欢迎使用腾讯语音合成服务。'


def tx_voice(text,voice_id):
    try:
        cred = credential.Credential(SecretId, SecretKey)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tts.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = tts_client.TtsClient(cred, "ap-shanghai", clientProfile)
        req = models.TextToVoiceRequest()
        request_data = {
            'Action': 'TextToVoice',
            'Version': '2019-08-23',
            'Region': 'ap-shanghai',
            'Text': text,
            'SessionId': str(uuid4()),
            'ModelType': 0,
            'Volume': 5,
            'Speed': 1,  # 控制语速  [-2.-1,0,1,2]
            'ProjectId': 0,
            'VoiceType': voice_id,  # 设置发音角色
            'PrimaryLanguage': 1,
            'SampleRate': 16000,
            'Codec': 'mp3',
            'Expired': 3600
        }
        req.from_json_string(json.dumps(request_data))
        resp = client.TextToVoice(req)
        # content为base64解码后的二进制流
        content = b64decode(resp.Audio)
        # I/O操作

        filename = './data/' + str(voice_id) + '.mp3'

        with open(filename, 'wb') as f:
            f.write(content)

    except TencentCloudSDKException as err:
        print(err)



list1 = [0,1,2,3,4,5,6,7,1001,1002,1003]

for i in list1:
    tx_voice(user_text,i)