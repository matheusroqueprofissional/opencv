import cv2 as cv

img = cv.imread("../../images/londres.jpg")
quadrado = cv.rectangle(img,(20,20),(80,80),(0,0,255),2)
cv.imshow("img",quadrado)

quadrado2 = cv.rectangle(img,(20,20),(80,80),(0,0,255),-1)
cv.imshow("img2",quadrado2)
#para salvar a imagem utilize o seguinte comando
#nao se esqueça de adicionar a extensao da imagem nova
#os parametros são (nome da nova imagem.extensao, qual imagem sera salva)
cv.imwrite("imagem_nova.jpg",quadrado2)
cv.waitKey(0)