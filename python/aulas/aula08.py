import cv2 as cv

img = cv.imread("../../images/londres.jpg")
cv.imshow("janelanormal",img[:2])
print(img.shape)
#com esse comando voce realiza o corte de uma parte determinada da imagem
#os parametros são [ponto inicial y: ponto final y, ponto inicial x: ponto final x]
corte = img[100:250,15:65]
cv.imshow("janela",corte)
cv.waitKey(0)