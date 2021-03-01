
import cv2

def tailor(in_img,out_img):  #截取字幕
    img = cv2.imread(in_img)
    print(img.shape)
    cropped = img[500:600, 100:750]  # 裁剪坐标为[y0:y1, x0:x1]
    imgray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    thresh = 200
    ret, binary = cv2.threshold(imgray, thresh, 255, cv2.THRESH_BINARY)  # 输入灰度图，输出二值图
    binary1 = cv2.bitwise_not(binary)  # 取反
    cv2.imwrite(out_img, binary1)

tailor('t1.jpg','t2.jpg')

