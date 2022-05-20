# c = open('canchito.txt', 'w')    #a=append es para agregar cosas al archivo/write es para agregar permisos

# c.write('\nagregaremos una nueva linea a nuestro archivo')

# c.close()

# x = open('canchito.txt')

# print(x.read())

import os

if os.path.exists('cachito.txt'):
    os.remove('canchito.txt')
else:
    print('el archivo no existe')

os.rmdir('micarpeta')