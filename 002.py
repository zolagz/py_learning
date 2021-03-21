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

"""


conf = configparser.ConfigParser()
conf.read("./conf/tcloud_auth.ini", encoding="UTF-8")

APPID = conf.getint("authorization", "AppId")
SecretId = conf.get("authorization", "SecretId")
SecretKey = conf.get("authorization", "SecretKey")


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
        'Text': '小王，五一小长假你打算去哪里玩啊',
        'SessionId': str(uuid4()),
        'ModelType': 0,
        'Volume': 5,
        'Speed': 0,
        'ProjectId': 0,
        'VoiceType': 0,
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
    with open('voice.mp3', 'wb') as f:
        f.write(content)

except TencentCloudSDKException as err:
    print(err)