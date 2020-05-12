'''
Created on 12 may. 2020

@author: Frodo
'''

import numpy as np
from numpy.lib.shape_base import column_stack

myList = [1, 2, 3]
type(myList)
print(type(myList))
# Las np arrays pueden tener varias dimensiones
array = np.array(myList)
print(type(array))
# Crear una matriz de tantas dimensiones, de 0 a 9, 10 elementos, se le puede poner un incremento
print(np.arange(0, 10))
print(np.arange(0, 10, 2))
# crear una matriz de varias dimensiones y relena con ceros, por defecto crea floats(filas,columnas)
print(np.zeros(shape=(5, 5)))

# crear una matriz de varias dimensiones y relena con unos, por defecto crea floats
print(np.ones(shape=(5, 5)))
# Crear numeros random
np.random.seed(101)
# Creamos random int (low,high, tamanho)
arr = np.random.randint(0, 100, 10)
print(arr)

# Creamos random int (low,high, tamanho)
arr2 = np.random.randint(0, 100, 10)
print(arr2)

# Maximo, minimo y media de una matriz

print(arr.max())
print(arr.argmax())
print(arr.min())
print(arr.mean())
# Tamanho, rango
print(arr.shape)

print(arr.reshape(2, 5))

# Creamos array de un cierto numero de dimensiones, y lo cambiamos
mat = np.arange(0, 100).reshape(10, 10)
print(mat)

# Seleccionar datos en concreto
row = 0
col = 1

print(mat[row, col])

# Seleccionar una columna entera o una fila

print(mat[:, 1])
print(mat[:10, 1])

print(mat[:, 1].reshape(10, 1))

print(mat)

mat[0:3, 0:3] = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

print(mat)

