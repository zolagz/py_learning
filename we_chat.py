import werobot
import os
import json
import configparser

from voice_dev.xun_fei import tts_say_wave


conf = configparser.ConfigParser()

conf.read("./conf.ini", encoding="UTF-8")
APP_ID = conf.getint("TENTCENT", "APP_ID")
APP_SECRET = conf.get("TENTCENT", "APP_SECRET")




robot = werobot.WeRoBot(token='tokenhere')

robot.config["APP_ID"] = APP_ID
robot.config["APP_SECRET"] = APP_SECRET

client = robot.client


# def upload_file2():
#     with open('data/001.png', 'rb') as f:
#         resp = Clinet.upload_media('image',f)
#         print(resp)
#
# def upload_file():
#     with open('data/1615705564865.wav', 'rb') as f:
#         resp = Clinet.upload_media('voice',f)
#         print(resp)



@robot.handler
def hello(message):
    # upload_file()
    msgId = tts_say_wave(message.Content)
    print(msgId)

    with open(msgId, 'rb') as f:
        resp = robot.client.upload_media('voice', f)
        print(resp['media_id'])
        # user_dic = json.dumps(resp)
        # print(user_dic['media_id'])
        resp = client.send_voice_message(message.source,resp['media_id'])
        print(resp)
    #
    # print(message.Content)
    # return 'Hello World!'

# 让服务器监听在 0.0.0.0:80




robot.config['HOST'] = '0.0.0.0'

robot.config['PORT'] = 8082

robot.run()



