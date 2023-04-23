import cv2 as cv

try:
 img=cv.imread("../../images/londres.jpg")
 cv.imshow("janela",img)
except:
    print("imagem não existe")
#codigo utilizado para alterar a cor da imagem
cinza = cv.cvtColor(img,cv.COLOR_BGR2GRAY) 
cv.imshow("cinza",cinza)
cv.waitKey(0)



