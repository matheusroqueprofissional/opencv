import cv2 as cv
i = cv.imread('../../images/grupodepessoas02.jpg')
iPB = cv.cvtColor(i, cv.COLOR_BGR2GRAY)
#Criação do detector de faces
df = cv.CascadeClassifier('../../xml/frontalface.xml')
#Executa a detecção
faces = df.detectMultiScale(iPB,
 scaleFactor = 1.05, minNeighbors = 7,
 minSize = (30,30), flags = cv.CASCADE_SCALE_IMAGE)
#Desenha retangulos amarelos na iamgem original (colorida)
for (x, y, w, h) in faces:
 cv.rectangle(i, (x, y), (x + w, y + h), (255, 0, 0), 1)
#Exibe imagem. Título da janela exibe número de faces
cv.imshow(str(len(faces))+' face(s) encontrada(s).',i)
cv.waitKey(0)
import pyttsx3

# Cria um objeto do motor de voz
engine = pyttsx3.init()

# Define a frase que você quer que o Python fale
phrase = "você tem",str(len(faces))+' faces encontradas'

# Faz o Python falar a frase
engine.say(phrase)
engine.runAndWait()

