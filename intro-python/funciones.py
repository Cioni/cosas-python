def miFuncion ():
    print('Mi primera funcion')

# miFuncion()

def imprimeDato(*nombre):
    print('El nombre completo es: ',nombre[1]) 

# imprimeDato('Chanchito','feliz','lala','lele')


def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

# nombreCompleto(nombre='chanchito', apellido='feliz')

def nombreCompleto2(**kwargs):  
    print(kwargs['nombre'], kwargs['apellido'])

# nombreCompleto2(nombre='chanchito', apellido='feliz')


def miFuncion2(argumento='chanchito'):
    print(argumento)

# miFuncion2('batman')
# miFuncion2()

def miFuncionLista(lista):
    for el in lista:
        print(el)

# miFuncionLista(['chanchito','feliz'])

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' ' 
        print(el)
    return i

# nombres = concatenaNombres(['chanchito', 'feliz'])
# print(nombres)

def recursion(i):
    if (i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)