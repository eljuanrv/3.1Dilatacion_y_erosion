#RIVERA VARGAS JUAN

from matplotlib import pyplot as plt
import numpy as np
import cv2
 
#Cargar la mascara
imagen = cv2.imread('star.png',0)
img2=cv2.imread('star.png',0)
#limpiar bordes
for i in range(0,3):
  #linea superior
  for j in range(0,imagen.shape[1]):
    if(imagen[i,j]==255):
      imagen[i,j]=0
  #linea izquierda
  for k in range(0,imagen.shape[0]):
    if(imagen[k,i]==255):
      imagen[k,i]=0

#limpiar bordes
for i in range(177,185):
  #linea inferior
  for j in range(0,imagen.shape[1]):
    if(imagen[i,j]==255):
      imagen[i,j]=0
  #linea derecha
  for k in range(0,imagen.shape[0]):
    if(imagen[k,i-4]==255):
      imagen[k,i-4]=0

#Erosion

#Crear un kernel de '1' de 6x6
kernel1 = np.ones((6,6),np.uint8)
 
#Se aplica la transformacion: Erode
erosion = cv2.erode(imagen,kernel1,iterations = 1)

#Dilatacion

kernel2 = np.ones((8,8),np.uint8)
#Se aplica la transformacion: Dilate
dilatacion = cv2.dilate(imagen,kernel2,iterations = 1)






titles = ['Original','Sin bordes','Erosion','Dilatacion']
images = [img2,imagen,erosion,dilatacion]
miArray = np.arange(4)
for i in miArray:
  plt.subplot(1,4,i+1),plt.imshow(images[i],'gray')
  plt.title(titles[i])
  plt.xticks([]),plt.yticks([])
 
plt.show()
