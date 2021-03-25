from pyperclip import copy
import zipfile
from os import rename
import os
import shutil
import requests
import getpass


# http://idea.medeming.com/jets/images/jihuoma.zip



download_dir = os.path.join(os.environ['HOME'] + os.sep, "Downloads")
# download_dir = getpass.getuser() + os.sep + 'Downloads'
request_url = 'http://idea.medeming.com/jets/images/jihuoma.zip'

file_name = download_dir + os.sep + 'jihuoma.zip'
unzip_finder = download_dir + os.sep + 'jihouma'

# 删除指定文件
os.remove(file_name)
# 删除文件夹
shutil.rmtree(unzip_finder)
# 解压
def unzip_file(zip_src,dst_dir):
    dst_dir = [dst_dir if dst_dir.endswith(os.sep) else dst_dir + os.sep][0]
    with zipfile.ZipFile(zip_src, 'r') as fd:
        for zfile in fd.namelist():
            gbkfilename = zfile.encode('cp437').decode('GBK')
            fd.extract(zfile, dst_dir)
            rename(''.join([dst_dir, zfile]), ''.join([dst_dir, gbkfilename]))

# 请求激活码并解压复制内容到粘贴板
def fetch_jets():
    request = requests.get(request_url)
    if request.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(request.content)
        unzip_file(file_name, unzip_finder)
        name1 = [unzip_finder + os.sep + f.title() for f in os.listdir(unzip_finder) if f.title().startswith('2018.2之后')][0]
        with open(name1, 'r', encoding='utf-8') as f:
            content = f.read()
            copy(content)
            print('文件已拷贝到粘贴板！！！')

    else:
        print('网络请求出错...')

fetch_jets()



