'''
Created on 14 may. 2020

@author: Frodo
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt


def cargar_immg():
    blank_img=np.zeros((600,600))
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(blank_img, text='ABCDE', org=(50, 300), fontFace=font, fontScale=5, color=(255, 255, 255), thickness=10)
    return blank_img


def mostrar(img):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()


img=cargar_immg()
mostrar(img)


kernel=np.ones((5,5), dtype=np.uint8)


''' ERODE: EROSIONA los boirdes de los objetos en primer plano, para acentuarlos, separar objetos unidos:
img, kernel, numero de iteraciones
'''
img_erode=cv2.erode(img,kernel,iterations=1)
mostrar(img_erode)


# anhadimos ruido blanco a la imagen, background noise

white_noise = np.random.randint(low=0,high=2,size=(600,600))
white_noise = white_noise*255
img_noise=white_noise+img
mostrar(img_noise)




''' OPENING: Tratar ruido brillante, con mas luz, sobre fondo oscuro, ruido de fondo tambien (EROSION + DILATION)'''
opening=cv2.morphologyEx(img_noise,cv2.MORPH_OPEN,kernel)
mostrar(opening)



# anhadimos ruido negro a la imagen, ruido en primer plano

black_noise = np.random.randint(low=0,high=2,size=(600,600))
black_noise = black_noise*-255 # afecta a los valores en blanco
img_noise=black_noise+img
img_noise[img_noise==-255]=0
print(img_noise.min())
mostrar(img_noise)


''' CLOSING: Tratar ruido brillante, con mas luz, sobre fondo oscuro, ruido EN PRIMER PLANO'''
closing=cv2.morphologyEx(img_noise,cv2.MORPH_CLOSE,kernel)
mostrar(closing)

''' GRADIENT: (EROSION-DILATION): dejar contornos y huevo dentro'''
gradient=cv2.morphologyEx(img_noise,cv2.MORPH_GRADIENT,kernel)
mostrar(gradient)
