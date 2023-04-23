import cv2 as cv

img = cv.imread("../../images/londres.jpg")
#coleta o tamanho da largura da imagem
width = int(img.shape[1])
#coleta o tamanho da altura da imagem
height = int(img.shape[2])
print("o shape da imagem é:\nlargura:",width,"\naltura:",height)
cv.imshow("imagemantiga",img)
#ajusta o tamanho para qual eu desejo
width = 300
height= 300
juntar_altura_largura = (width,height)
resize = cv.resize(img,juntar_altura_largura, interpolation=cv.INTER_AREA)
print("o shape da nova imagem é:\nlargura:",width,"\naltura:",height)
cv.waitKey(0)