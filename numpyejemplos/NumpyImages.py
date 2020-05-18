
'''
Created on 12 may. 2020

@author: Frodo
'''

import numpy as np

import matplotlib.pyplot as plt

from PIL import Image  
from numpy.lib.function_base import place

pic = Image.open(r"C:\Users\Frodo\eclipse-workspace\DATA\00-puppy.jpg")

print(type(pic))

# La transformamos en un array
pic_arr = np.array(pic)
print(type(pic_arr))
print(pic_arr.shape)
plt.imshow(pic_arr)
plt.show()

# Hacemos una copia de la imagen
pic_red = pic_arr.copy()
# R G B
print(pic_red.shape)

# Red color, valores cercanos al cero (no hay rojo), negro, 255 full rojo
'''RED CHANNEL'''
print(pic_red[:,:,0])
plt.imshow(pic_red[:,:,0],cmap='gray') # en escala de grises cuanto mas claro, mas rojo en esta imagen
plt.show()
'''GREEN CHANNEL'''
print(pic_red[:,:,1])
plt.imshow(pic_red[:,:,1],cmap='gray') # en escala de grises cuanto mas claro, mas verde en esta imagen
plt.show()
'''BLUE CHANNEL'''
print(pic_red[:,:,2])
plt.imshow(pic_red[:,:,1],cmap='gray') # en escala de grises cuanto mas claro, mas azul en esta imagen
plt.show()



# Jugar con los colores cambiando los valores del array de R G B
'''Valores del verde a 0'''
pic_red[:,:,1] =0
plt.imshow(pic_red)
plt.show()

'''Valores del azul a 0'''
pic_red[:,:,2] =0
plt.imshow(pic_red) 
plt.show()


