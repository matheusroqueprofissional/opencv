import cv2 as cv
i = cv.imread('../../images/grupodepessoas02.jpg')
df = cv.CascadeClassifier("../../xml/frontalface.xml")
faces = df.detectMultiScale(i,scaleFactor = 1.05, minNeighbors= 7,
                            minSize = (30,30), flags=cv.CASCADE_SCALE_IMAGE)
for (x,y,h,w) in faces:
    cv.rectangle(i,(x,y),(x+w,y+h),(0,0,255),1)
cv.imshow("janela",i)
cv.waitKey(0)



