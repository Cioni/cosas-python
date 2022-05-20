i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)  

usuarios = ['chanchito feliz', 'felipe', 'roberto', 'nicolas']

for usuarios in usuarios:
    print(usuarios)

usuario = 'chanchito feliz'

for c in usuario:
    print(c)

 
usuarios = ['chanchito feliz', 'felipe', 'roberto', 'nicolas']

for usuario in usuarios:
    if usuario == 'roberto':
        break
    print(usuario )

usuarios = ['chanchito feliz', 'felipe', 'roberto', 'nicolas']

for usuario in usuarios:
    if usuario == 'roberto':
        continue
    print(usuario )

for x in range(3,30,3):
    print(x)
else:
    print('Hemos terminado')

usuarios = ['chanchito feliz', 'felipe', 'roberto', 'nicolas'] 

edades = [24, 25, 26, 35]

for usuario in usuarios:
    for edad in edades:
        print(usuario,edad)

