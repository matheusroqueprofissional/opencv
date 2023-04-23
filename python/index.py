import cv2 as cv
import sys

img = cv.imread("../images/londres.jpg")

if img is None:
    sys.exit("Não pude encontrar a imagem")
cv.imshow("Display window",img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("starry_night.png",img)