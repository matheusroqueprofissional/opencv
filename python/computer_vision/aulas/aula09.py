import cv2 as cv

local = "../../images/londres.jpg"
img = cv.imread(local)
#ele ira aplicar o efeito blur com esse comando
#os parametros de cv.blur são (imagem que o cvimread le, quanto voce quer que estique no eixo x e quanto voce quer que estique no eixo y)
filter_blur=cv.blur(img,ksize=(100,100))
cv.imshow("filtro",filter_blur)
cv.waitKey(0)
