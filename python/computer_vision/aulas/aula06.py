import cv2 as cv

img = cv.imread("../../images/londres.jpg")
quadrado = cv.rectangle(img,(20,20),(80,80),(0,0,255),2)
cv.imshow("img",quadrado)

#caso voce queira para pintar o quadrado por dentro apenas altere o ultimo parametro para -1
quadrado2 = cv.rectangle(img,(20,20),(80,80),(0,0,255),-1)
cv.imshow("img2",quadrado2)
cv.waitKey(0)