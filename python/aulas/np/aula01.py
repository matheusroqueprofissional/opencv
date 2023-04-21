import numpy as np
import cv2 as cv
print("codigo iniciado\n")
img = cv.imread("../../../images/londres.jpg")
mascara = np.zeros(img.shape)
mascara2 = np.zeros(img.shape[:2],dtype = "uint8")
print("mascara 01 ====================================")
print(mascara)
print("mascara 02 ====================================")
print(mascara2)
