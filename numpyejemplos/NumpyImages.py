'''
Created on 12 may. 2020

@author: Frodo
'''

import numpy as np

import matplotlib.pyplot as plt

from PIL import Image  
from numpy.lib.function_base import place

pic = Image.open(r"C:\Users\Frodo\Downloads\timbre.png")

print(type(pic))

# la transformamos en un array
pic_arr = np.array(pic)
print(type(pic_arr))
print(pic_arr.shape)
plt.imshow(pic_arr)
plt.show()

#Hacemos una copia de la imagen
pic_red = pic_arr.copy()
plt.imshow(pic_red)
plt.show()

# R G B
print(pic_red.shape)

# Red color, valores cercanos al cero (no hay rojo), negro, 255 full rojo
print(pic_red[:,:,0])
plt.imshow(pic_red[:,:,0],cmap='gray') # en escala de grises cuanto más claro, más rojo en esta imagen
plt.show()

# Green color
plt.imshow(pic_red[:,:,1])
plt.show()

# Blue color
plt.imshow(pic_red[:,:,2])
plt.show()

# Jugar con los colores cambiando los valores del array de R G B