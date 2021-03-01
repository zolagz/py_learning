 platformName ：声明是ios还是Android系统

platformVersion ： Android内核版本号，可通过命令查看
adb shell getprop ro.build.version.release



deviceName ：连接的设备名称，通过命令adb devices -l中model查看

appPackage ：apk的包名

appActivity：apk的launcherActivity，通过命令adb shell dumpsys activity | findstr “mResume”查看（需先打开手机应用）



注意：Android 8.1之前应使用adb shell dumpsys activity | findstr “mFocus”

3.运行Start Session，选择元素