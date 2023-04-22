import cv2 as cv
import numpy as np
print("nesse codigo iremos tentar desenvolver um codigo capaz de identificar\n",
       "um rosto humano e desenhar linhas no rosto e nos olhos")

img =cv.imread("../../../images/grupodepessoas02.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
shape = img.shape
tamanho = (600,600)
resizeimage = cv.resize(img,tamanho,interpolation=cv.INTER_AREA)
df = cv.CascadeClassifier("../../../xml/frontalface.xml")
ey = cv.CascadeClassifier("../../../xml/haarcascade_eye.xml")
faces = df.detectMultiScale(resizeimage,scaleFactor = 1.05, minNeighbors= 5,
                            minSize = (20,20), flags=cv.CASCADE_SCALE_IMAGE)

contadorface = 0
contadoreyes = 0
kernel = (3,3)
for (x,y,w,h) in faces:
    contadorface= contadorface+1
    cv.rectangle(resizeimage,(x,y),(x+w,+y+h),(0,0,255),1)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = resizeimage[y:y+h, x:x+w]
    eyes = ey.detectMultiScale(roi_color, scaleFactor=1.07, minNeighbors=7, minSize=(50, 50), maxSize=(100, 100))

    for(ex,ey,ew,eh) in eyes:
        contadoreyes = contadoreyes+1
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

#0 altura
#1 largura
print(shape)
cv.imshow("janela",resizeimage)
cv.waitKey(0)
import pyttsx3

# Cria um objeto do motor de voz
engine = pyttsx3.init()



# Faz o Python falar a frase
engine.say(f"a imagem tem {contadorface} faces e {contadoreyes} olhos possiveis de detectar")
engine.runAndWait()