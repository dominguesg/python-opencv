import cv2
import random

img = cv2.imread(
    "assets/background.png", cv2.IMREAD_UNCHANGED
)  # carrega a imagem para a memória

# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [
#             random.randint(0, 255),
#             random.randint(0, 255),
#             random.randint(0, 255),
#             random.randint(0, 255)
#         ]

tag = img[500:700, 600:900] #copia um quadrado iniciando no coluna 500 até 700 (intervalo aberto) e linha 600 até 900 (intervalo aberto)

img[100:300, 650:950] = tag #cola tag nesta área (img[100:300, 650:950]) da imagem

cv2.imshow("Image", img)  # Cria uma janela. 'Image' = nome da janela
cv2.waitKey(
    0
)  # Esperar por qualquer tecla por tempo indefinido. Numero n é em segundos
cv2.destroyAllWindows  # Destroi os processos de todas as janelas criadas pelo programa
