from flask import Flask,request
import time
import os
import subprocess
import cv2
import requests
import base64


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data/upload_dir'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','mp3','py'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


@app.route('/upload',methods=['POST'])
def upload_file():
    file = request.files['file']
    print(file)
    print(str(file))
    # return "oooook"
    if file and allowed_file(file.filename):
        ext_name = file.filename.split('.')[1]
        f_name = str(int(round(time.time() * 1000)))+"." + ext_name
        file.save(os.path.join(make_dir(app.config['UPLOAD_FOLDER']),f_name))
        return {'fileName':f_name}
    return {'msg:' '不支持该文件类型上传！'}

@app.route('/hi')
def hello():
    return "Hello world"

# 提取单张图片文本
@app.route('/imgText',methods=['POST'])
def img_text():
    pass


def requestApi(img):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    params = {"image": img, 'language_type': 'CHN_ENG'}
    access_token = '需要需改'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    results = response.json()
    return results

# 读取图片&字幕操作

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        # 将读取出来的图片转换为b64encode编码格式
        return base64.b64encode(fp.read())


# 视频提取图片
@app.route('/transImg',methods=['POST'])
def video_trans_img():
    video_name = request.form['videoName']
    fileNmae = video_name.split('.')[0]
    out_path = app.config['UPLOAD_FOLDER'] + '/' +fileNmae
    input_file =  app.config['UPLOAD_FOLDER'] + '/' + video_name

    if os.path.exists(input_file):
        out_path = make_dir(out_path)
        out_img = "%s/%s.jpg" %(out_path,'img_%0005d')
        out_path = out_img.rstrip("/")
        cmd = "ffmpeg -i %s -r 1 -f image2 %s" % (input_file,out_path)
        res = subprocess.call(cmd,shell=True)
        if res !=0:
            return {'status':'400','msg':'错误了'}
        else:
            return {'status':'200','img_path':fileNmae}

    else:
        return {'msg':'文件不存在'}

def subtitles(in_img,out_img):  #截取字幕
    # image_list = os.listdir(in_img)
    # image_list.remove('.DS_Store')
    # image_list.sort()

    image_list = [in_img + '/' + img for img in os.listdir(in_img) if img.endswith(".jpg")]
    for img_file in image_list:
        print(in_img + "/" + img_file)
        img = cv2.imread(in_img + "/" + img_file)
        y0 = img.shape[0] - 100
        y1 = img.shape[0]
        x0 = 100
        x1 = img.shape[1] - 50
        cropped = img[y0: y1, x0: x1]  # 裁剪坐标为[y0:y1, x0:x1]

        imgray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
        thresh = 200
        ret, binary = cv2.threshold(imgray, thresh, 255, cv2.THRESH_BINARY)  # 输入灰度图，输出二值图
        binary1 = cv2.bitwise_not(binary)  # 取反
        cv2.imwrite(out_img +"/" + img_file, binary1)


#  判断中文
# 定义一个函数，用来判断是否是中文，是中文的话就返回True代表要提取中文字幕
def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


@app.route('/getText',methods=['POST'])
def for_text():
    video_name = request.form['videoName']
    array = []  # 定义一个数组用来存放words

    video_name = app.config['UPLOAD_FOLDER'] + '/' + video_name
    images = os.listdir(video_name)
    # images.remove('.DS_Store')
    images.sort()
    for img in images:
        img_path = video_name+'/'+img
        img_content = get_file_content(img_path)
        try:
            results = requestApi(img_content)['words_result']  # 调用requestApi函数，获取json字符串中的words_result
            for item in results:
                print(item)
                if is_Chinese(item['words']):
                    array.append(item['words'])  # 将图片中不需要的字幕“猎奇笔记本”替换为空
        except Exception:
            pass
    text = ''
    result = list(set(array))  # 将array数组准换为一个无序不重复元素集达到去重的效果，再转为列表
    result.sort(key=array.index)  # 利用sort将数组中的元素即字幕重新排序，达到视频播放字幕的顺序
    for item in result:
        # print(item)
        text += item+'\n'

    return {'result':text}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

