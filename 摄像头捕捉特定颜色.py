# 摄像头捕捉指定颜色程序
# 需要安装图像处理库 OpenCV2
# 需要安装科学计算工具 numpy
import cv2
import numpy as np
cap = cv2.VideoCapture(0)# set blue thresh
lower_blue=np.array([105,43,46])    #三通道HSV
upper_blue=np.array([150,255,255])

while(1):    # get a frame and show
    ret, frame = cap.read()
    cv2.imshow('Capture', frame)    # change to hsv model
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    # get mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow('Mask', mask)    # detect blue
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Result', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        breakcap.release()
cv2.destroyAllWindows()
