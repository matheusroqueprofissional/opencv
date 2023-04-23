import cv2 as cv

img = cv.imread("../../images/londres.jpg")
#o codigo abaixo mostra como desenhar um circulo na imagem
#os parametros são a imagem que sera analisada, a localização(x,y) do centro do circulo,o tamanho do circulo, a cor, o tamanho do risco(quanto maior mais pra dentro do circulo o risco ficara)
quadrado = cv.circle(img,(50,50),20,(255,0,0),10)
cv.imshow("janela",img)
cv.waitKey(0)