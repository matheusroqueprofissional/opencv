
#! mascara
#! Primeiro é importante definir que uma máscara nada mais é que uma imagem onde cada pixel pode estar “ligado” ou “desligado”, ou seja, a máscara possui pixels pretos e brancos apenas

import cv2 as cv
import numpy as np
img = cv.imread("../../images/londres.jpg")
cv.imshow("img",img)
# esse script é usado para criar uma imagem de acordo com a variavel img
# futuramente falaremos sobre matrizes
mascara = np.zeros(img.shape[:2], dtype = "uint8")
position_width = 90
position_height = 120
cv.circle(mascara,(position_width,position_height),80,255,-1)
img_com_mascara = cv.bitwise_and(img,img,mask=mascara)
cv.imshow("mascara",img_com_mascara)
cv.waitKey(0)






