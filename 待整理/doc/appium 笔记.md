
Appium 常用方法总结 (python 版)
 
1、app后台运行

driver.background_app(5) 

2、锁屏

driver.lock(5) 

3、隐藏键盘

driver.hide_keyboard() 

4、启动一个app或者在当前app中打开一个新的activity，仅适用于android

driver.start_activity('com.example.android.apis', '.Foo') 

5、检查app是否被安装

driver.is_app_installed('com.example.android.apis') 

6、安装app

driver.install_app('path/to/my.apk') 

7、卸载app

driver.remove_app('com.example.android.apis') 

8、关闭app

driver.close_app(); 

9、启动app

driver.launch_app()