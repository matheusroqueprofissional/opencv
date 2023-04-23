
#! esse script por ele ser mais complexo eu irei explicar ele linha por linha

#?aqui realizamos as importacoes necessarias, no caso o opencv
import cv2 as cv
#?definimos a imagem que será analizada
i = cv.imread('../../images/grupodepessoas02.jpg')
#? alteramos a cor da imagem para cinza para a imagem ficar melhor analizada
iPB = cv.cvtColor(i, cv.COLOR_BGR2GRAY)
#Criação do detector de faces
#?atravez do metodo CascadeClassifier 
df = cv.CascadeClassifier('../../xml/frontalface.xml')
#Executa a detecção
#? nesse caso(
#? ipb é a imagem que sera detectada as imagens
#? SCALEFACTOR é um parâmetro que controla a escala da imagem que será usada na detecção de faces. Ele determina o tamanho da imagem que será usada no próximo estágio do classificador em cascata. Valores menores aumentam a sensibilidade da detecção, mas também aumentam o tempo de processamento. 
#? Minneighbors  é o número mínimo de vizinhos que cada retângulo candidato deve ter para ser considerado uma face. Este parâmetro controla a sensibilidade da detecção, aumentando ou diminuindo o número de detecções falsas. 
#? minSize é o tamanho mínimo que uma face deve ter para ser detectada. Este parâmetro ajuda a ignorar regiões muito pequenas que não são faces, economizando tempo de processamento. 
#? é um parâmetro que controla o modo de escala da imagem. Existem vários modos possíveis, mas o modo cv.CASCADE_SCALE_IMAGE é o mais comum. Ele define que a imagem será escalada de forma linear, sem usar uma pirâmide Gaussiana.
#? )


#TODO scaleFactor controla a sensibilidade da detecção de objetos, aumentando ou diminuindo o tamanho da imagem que será usada na análise.
#TODO MINSIZE O parâmetro minSize é usado para controlar o tamanho mínimo que um objeto, como um rosto, deve ter para ser considerado válido. No caso específico do exemplo dado, o valor (30, 30) indica que qualquer objeto menor que 30x30 pixels não será considerado um objeto válido e não será detectado.
#TODO FLAGS O parâmetro flags é usado para controlar o comportamento da detecção de objetos, como rostos. O valor cv.CASCADE_SCALE_IMAGE indica que a detecção de objetos será feita usando uma imagem escalada, em vez de uma imagem em tamanho real.
#! OU SEJA NESSA FUNCAO É RESPONDAVEL POR DEFINIR A SENSIBILIDADE DA ANALISE A SER FEITA
faces = df.detectMultiScale(iPB,
 scaleFactor = 1.05,w minNeighbors = 7,
 minSize = (30,30), flags = cv.CASCADE_SCALE_IMAGE)
print(faces)
#Desenha retangulos amarelos na iamgem original (colorida)
#?a funcao faces retorna para nos informaçoes assim: [ 33 130  49  49]
#? o que seriam informacoes de aonde inicia (x,y)
for (x, y, w, h) in faces:
 contador = 0
 contador=contador+1
 print(f"face:{contador}\nX:{x}\nY:{y}\nW:{w}\nH:{h}")
 cv.circle(i,(x+25,y+25),(30),(0,255,0),3)
 cv.rectangle(i,(x,y),(x+w,y+h),(0,0,255),3)
#Exibe imagem. Título da janela exibe número de faces
cv.imshow(str(len(faces))+' face(s) encontrada(s).',i)
cv.waitKey(0)



