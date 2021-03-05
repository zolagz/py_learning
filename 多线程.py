import threading
import time


def down_video(url,title):
    print("开始下载   " + title + " " + url + '\n')
    time.sleep(3)
    print("下载完成   " +  title + " " + url + '\n')

threadpool = []
title_list = []


t1 = time.time()
for i in range(10):

    url = "http://" + str(i ** 10 )
    # down_video(url,item)
    # # 定义线程
    th = threading.Thread(target=down_video, args=(url, str(i)))
    # 将线程加入线程池
    threadpool.append(th)
#
# 开始线程
for th in threadpool:
    th.start()
# 等待所有线程运行完毕
for th in threadpool:
    th.join()


t2 = time.time()

print(t2 -t1 )