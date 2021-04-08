import requests
import json
import urllib3

urllib3.disable_warnings()

home_url = 'https://api.tuchong.com/2/feed-app'

detail_url = 'https://api.tuchong.com/2/sites/'

work_url = 'https://api.tuchong.com/sites/16389644/works'

header = {
    'User-Agent': 'okhttp/3.12.2 com.ss.android.tuchong (Tuchong: 7020 7.2.0) (Android: 6.0.1 23)',
    # 'device': '2129094747357496',
    'version': '7020',
    'channel': 'xiaomi',
    'platform': 'android',
    'Host': 'api.tuchong.com',
    # 'Connection': 'Keep-Alive',
    # 'Accept-Encoding': 'gzip',
    # 'host-address': '192.168.199.29',
    # 'host-name': '192.168.199.29',
}

paramer = {
    # 'mac_address': '08:00:27:5A:1B:E2',
    'language': 'zh',
    'resolution': '1170*1872',
    # 'device_type': 'MuMu',
    'device_platform': 'android',
    'os_api': '23',
    'device_brand': 'Android',
    'openudid': '9c785ac7a446e8f7',
    # '_rticket': '1617873510230',
    'post_id': '85567904',
    'version_code': '7020',
    'version_name': '7.2.0',
    # 'ac': 'wifi',
    # 'aid': '1130',
    # 'dpi': '416',
    # 'iid': '1830027601666567',
    # 'cdid': 'eaa69cde-464b-4621-bbb5-a72f147ff3f0',
    'page': '1',
    'type': 'loadmore',
    # 'uuid': '1130',
    # 'device_id': '2129094747357496',
    # 'ssmix': 'a',
    # 'before_timestamp': '0',
    'show_moment': '0',
    'os_version': '6.0.1',
    'channel': 'xiaomi',
    'video_id': '7536632',
    'app_name': 'tuchong',
    # 'update_version_code': '7020',
    # 'new-feed': '1',
    # 'manifest_version_code': '7020',

}


response = requests.get(home_url, headers= header,params= paramer,verify=False)

if response.status_code == 200:
    result = response.json()
    counts = result['counts']
    for i in result['feedList']:
        if i['type'] == 'post':
            # print(i['entry']['images'])
            for v in i['entry']['topics']:
                # print(v['title'])
                # print(v['description'])
                img_url = v['cover_url']
                res_img = requests.get(url=img_url,verify=False)
                name = img_url.rsplit('/')[-1]
                file_name = 'img/'  + name

                with open(file_name,'wb') as f:
                    f.write(res_img.content)
                print(img_url)
