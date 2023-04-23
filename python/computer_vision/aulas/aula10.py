
#!nesse codigo aprenderemos a usar a função resize do opencv
import cv2 as cv
import numpy as np


# Reading an image
img = cv.imread('../../images/londres.jpg')
print("dimensoes imagem original:\ny:",img.shape[0],"\nx:",img.shape[1])
cv.imshow("t",img)
print("============================")
largura = img.shape[1]
altura = img.shape[0]
largura_nova = 320
altura_nova = 320
img_resize = cv.resize(img,(largura_nova,altura_nova),interpolation=cv.INTER_AREA)
cv.imshow("resize",img_resize)
cv.waitKey(0)
