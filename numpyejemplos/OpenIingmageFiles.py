'''
Created on 12 may. 2020

@author: Frodo
'''

import cv2
img = cv2.imread(r"C:\Users\Frodo\Downloads\mascarilla.jpg")
cv2.imshow('Mascarilla',img)

# tecla para poder cerrar la ventana
cv2.waitKey()
# En linux a veces ocurre que no puedes cerrar la imagen, restart el kernel para que funcione


while True:
    cv2.imshow('Mascarilla',img)
    # si esperamos al menos 1 ms y presionamos la tecla de escape salimos del loop
    if cv2.waitKey(1) & 0xFF ==27: # 0xFF = 11111111
        break

cv2.destroyAllWindows()