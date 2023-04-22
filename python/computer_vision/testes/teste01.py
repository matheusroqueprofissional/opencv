import cv2 as cv
import numpy as np
print("nesse codigo iremos tentar desenvolver um codigo capaz de identificar\n",
       "um rosto humano e desenhar linhas no rosto e nos olhos")

img =cv.imread("../../../images/rosto_negro01.jfif")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
shape = img.shape
tamanho = (600,600)
resizeimage = cv.resize(img,tamanho,interpolation=cv.INTER_AREA)
df = cv.CascadeClassifier("../../../xml/frontalface.xml")
ey = cv.CascadeClassifier("../../../xml/haarcascade_eye.xml")
faces = df.detectMultiScale(resizeimage,scaleFactor = 1.05, minNeighbors= 7,
                            minSize = (30,30), flags=cv.CASCADE_SCALE_IMAGE)

contador = 0

for (x,y,w,h) in faces:
    contador= contador+1
    cv.rectangle(resizeimage,(x,y),(x+w,+y+h),(0,0,255),1)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = resizeimage[y:y+h, x:x+w]
    eyes = ey.detectMultiScale(roi_color, scaleFactor=1.07, minNeighbors=7, minSize=(50, 50), maxSize=(100, 100))

    for(ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

#0 altura
#1 largura
print(shape)
cv.imshow("janela",resizeimage)
cv.waitKey(0)