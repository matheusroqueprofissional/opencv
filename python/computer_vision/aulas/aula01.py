import cv2 as cv #importando cv2 definindo nome de chamada para cv
import sys
caminho_pasta_img = "../../images/"
nome_do_arquivo = "londres.jpg"
caminho_completo = caminho_pasta_img+nome_do_arquivo

img = cv.imread(caminho_completo) #apontando qual imagem sera analizada pelo opencv

#se nao tiver imagem ou se ela for nula
if img is None:
    print("imagem não encontrada")
#mostrando imagem
cv.imshow("londres",img)
k = cv.waitKey(0)

    