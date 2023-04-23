import cv2

# Inicialize a webcam usando o índice padrão da câmera (normalmente 0)
cap = cv2.VideoCapture(0)

# Verifique se a câmera foi aberta corretamente
if not cap.isOpened():
    raise IOError("Não foi possível abrir a câmera")

# Loop para ler cada quadro da webcam
while True:
    # Leia o próximo quadro da câmera
    ret, frame = cap.read()

    # Se o quadro não puder ser lido, saia do loop
    if not ret:
        break
    df = cv2.CascadeClassifier("../../../xml/frontalface.xml")
    ey = cv2.CascadeClassifier("../../../xml/haarcascade_eye.xml")
    faces = df.detectMultiScale(frame,scaleFactor = 1.05, minNeighbors= 5,
                             flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        eyes = ey.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=3)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'face'
        text_size = cv2.getTextSize(text, font, 1, 2)[0]
        text_x = int(x + (w - text_size[0]) / 2)
        text_y = y + h + 30
        cv2.putText(frame, text, (text_x, text_y), font, 1, (0, 0, 255), 1, cv2.LINE_AA)

        for(ex,ey,ew,eh) in eyes:
            font2 = cv2.FONT_HERSHEY_SIMPLEX
            text2 = 'olho'
            text_size2 = cv2.getTextSize(text, font, 1, 2)[0]
            text_x2 = int(ex + (ew - text_size[0]) / 2)
            text_y2 = ey + eh + 30
            center = ((ex + ex + ew)//2,  (ey + ey + eh)//2 )
            radius = max(ew, eh)//2
            cv2.circle(frame, center, radius, (0, 255, 0), 2)
            cv2.putText(frame, text2, (text_x2, text_y2), font2, 1, (255, 0, 0), 1, cv2.LINE_AA)


            cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
            
    # Mostre o quadro em uma janela
    frame2 =cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    frame3 =cv2.cvtColor(frame,cv2.COLOR_RGB2LAB)
    cv2.imshow('Input1', frame)
    cv2.imshow('Input2', frame2)
    cv2.imshow('Input3', frame3)


    # Aguarde 1 milissegundo e verifique se a tecla 'Esc' foi pressionada
    c = cv2.waitKey(1)
    if c == 27:
        break

# Libere a câmera e feche todas as janelas
cap.release()
cv2.destroyAllWindows()
