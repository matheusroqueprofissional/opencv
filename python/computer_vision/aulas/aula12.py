import cv2 as cv
import numpy as np

img = cv.imread("../../images/londres.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("L*a*b*", lab)
cv.waitKey(0)