# dato = input('ingrese dato: ')

# lista = ['hola', ',imdp', 'chanchito', 'feliz', 'dragones']

# if lista.count(dato) > 0:
#     print('El dato existe: ', dato)
# else:
#      print('El dato no existe :(', dato)

primero = input('ingrese primer numero: ')

try: 
    primero = int(primero)
except:
    primero = 'chanchito feliz'

if primero=='chanchito feliz':
    print('el valor ingresado no es un entero')
    exit()

segundo = input('Ingrese segundo numero')

try: 
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'    

if segundo=='chanchito feliz':
    print('el valor ingresado no es un entero')
    exit()

simbolo = input('ingrese operacion: ')

if simbolo == '+':
    print('suma: ',primero + segundo)
elif simbolo == '-':
    print('resta: ',primero - segundo)
elif simbolo == '*':
    print('multiplicacion: ',primero * segundo)
elif simbolo == '/':
    print('division: ',primero / segundo)
else:
    print('El simbolo ingresado no es valido')