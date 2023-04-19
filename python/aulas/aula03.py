import cv2 as cv

img = cv.imread("../../images/londres.jpg")
cv.imshow("bgr",img)
cinza = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("cinza",cinza)
bgr = cv.cvtColor(img,cv.COLOR_RGB2BGR)
cv.imshow("rgb",bgr)
#o comando abaixo é usado para desenhar uma linha na imagem
#na posição x = 0 e y = 10 inicia a linha e ela ira até a posição x=50 y= 20 na imagem
#o ultimo parametro indica a expessura da linha
quadrado = cv.line(img,(0,10),(50,20),(0,255,0),2)
cv.imshow("quadrado_rgb",quadrado)
quadrado = cv.line(cinza,(0,10),(50,20),(0,255,0),2)
cv.imshow("quadrado_cinza",quadrado)
quadrado = cv.line(bgr,(0,10),(50,20),(0,255,0),2)
cv.imshow("quadrado_bgr",quadrado)
cv.waitKey(0)