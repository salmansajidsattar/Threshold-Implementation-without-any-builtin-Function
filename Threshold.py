import cv2 as cv
path='DATA\\v3.mp4'
print('VIDEO PATH',path)
cap=cv.VideoCapture(path)
while True:
    ret,frame=cap.read()
    if ret is False:
        break
    frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    for i in range(720):
        for j in range(1280):
            if ((frame[i, j] >= 15) and (frame[i, j] <= 100)):
                frame[i, j]=255;
            else:
                frame[i,j]=0;
    cv.imshow('IMAGE',frame)
    k=cv.waitKey(1)
    print('1')
    if k is ord('q'):
        break
