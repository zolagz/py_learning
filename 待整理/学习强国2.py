from appium import webdriver
import time
import random
from selenium.webdriver.common.by import By

title_item_list = ['推荐', '要闻', '新思想', '北京', '综合','县级融合']

video_channel_list = ['第一频道', '学习视频', '联播频道', '看党史']

def init_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0.1'
    desired_caps['deviceName'] = 'emulator-5554'
    desired_caps['appPackage'] = 'cn.xuexi.android'
    desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'
    desired_caps['noSign'] = True
    desired_caps['noReset'] = True
    desired_caps['newCommandTimeout'] = 3600
    return desired_caps

def swipe_to_up(driver):
    print("向上滑动......")
    window_size = driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    time.sleep(1.2)
    driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)




def read_articles():
    print("开始阅读文章.....")
    for title in title_item_list:
        t1 = "//android.widget.TextView[contains(@text, '%s')]" % title
        driver.find_element_by_xpath(t1).click()
        print("点 击 了--- %s " % title)
        time.sleep(4)
        try:
            list_view = driver.find_elements_by_class_name('android.widget.TextView')
            for v in list_view:
                if len(v.text) > 10:
                    print(v.text)
                    vBtn = driver.find_element_by_xpath("//*[contains(@text, '%s')]" % v.text)
                    if len(vBtn.get_attribute('resourceId')) !=0:
                        print("点击......看文章详情 .....")
                        vBtn.click()
                        time.sleep(2)
                        swipe_to_up(driver)
                        time.sleep(3)
                        swipe_to_up(driver)
                        # 随机看文章65 - 75秒
                        sTime = random.randint(65, 75)
                        time.sleep(sTime)
                        driver.keyevent(4)
                        print("退出看文章")

        except:
            print("发生了异常")
    print("文章阅读完毕......")




def pass_method(driver):
    # list_view = driver.find_elements_by_class_name('android.widget.ListView')
    list_view = driver.find_elements_by_xpath('//android.webkit.WebView[@content-desc="学习积分"]/android.widget.ListView/android.view.View')

    for lv in list_view:

        print('xxxxx' * 6)
        l = lv.find_elements_by_class_name('android.view.View')
        # print(len(l))
        if len(l) == 5:
            name_1 = l[0].get_attribute('content-desc')
            name_2 = l[1].get_attribute('content-desc')
            name_3 = l[2].get_attribute('content-desc')
            name_4 = l[3].get_attribute('content-desc')
            print("name_1 %s" % name_1)
            print("name_2 %s" % name_2)
            print("name_3 %s" % name_3)
            print("name_4 %s" % name_4)

if __name__ == '__main__':
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', init_driver())
    driver.implicitly_wait(60)
    # time.sleep(7)
    # read_articles()
    driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '我的')]").click()
    print('点击 -- 我的 ')
    driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '学习积分')]").click()
    print('点击 -- 学习积分 ')
    # //android.webkit.WebView[@content-desc="学习积分"]/android.widget.ListView/android.view.View[1]
    #
    # //android.view.View[@content-desc="成长总积分"]
    btn_1 = driver.find_element_by_xpath('//android.view.View[@content-desc="成长总积分"]')
    print(btn_1.location)
    print(btn_1.location.get('x'))
    print(btn_1.location.get('y'))
    btn_2 = driver.find_element_by_xpath('//android.view.View[@content-desc="登录"]')
    print(btn_2.location)
    print("拖动")
    driver.swipe(btn_1.location.get('x'),btn_2.location.get('y'),btn_1.location.get('x'),btn_1.location.get('y'),500)
    # Using XPath locators is


    lv = driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="学习积分"]/android.widget.ListView/android.view.View[5]')

    l = lv.find_elements_by_class_name('android.view.View')
    if len(l) == 5:
        name_1 = l[0].get_attribute('content-desc')
        name_2 = l[1].get_attribute('content-desc')
        name_3 = l[2].get_attribute('content-desc')
        name_4 = l[3].get_attribute('content-desc')
        l[3].click()
        print("name_1 %s" % name_1)
        print("name_2 %s" % name_2)
        print("name_3 %s" % name_3)
        print("name_4 %s" % name_4)

    time.sleep(3)


    # t1 = driver.find_element_by_class_name('android.webkit.WebView').text
    # print(t1)

    # // *[ @ id = "app"] / div / div / div[2] / div[1] / div / section[1] / div / div