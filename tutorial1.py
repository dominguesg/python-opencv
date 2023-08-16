import cv2

img = cv2.imread('assets/background.png', cv2.IMREAD_UNCHANGED) #carrega a imagem para a memória

# img = cv2.resize(img, (1280,720)) #Determina o tamanho exato da imagem
img = cv2.resize(img, (0,0), fx=0.2, fy=0.2) #Determina o tamanho colocando um multiplicador em X e Y da imagem

img = cv2.rotate(img, cv2.ROTATE_180) # rotaciona a imagem

cv2.imwrite('assets/new_background.png', img) #Salva a imagem em um novo arquivo no diretorio

cv2.imshow('Image', img) #Cria uma janela. 'Image' = nome da janela
cv2.waitKey(0) #Esperar por qualquer tecla por tempo indefinido. Numero n é em milisegundos
cv2.destroyAllWindows #Destroi os processos de todas as janelas criadas pelo programa
