class Usuario:    
 def __init__(self, nombre, apellido):   # self es usado para instancias 
    self.nombre = nombre
    self.apellido = apellido
 def saludo(self):
     print('hola, el nombre es', self.nombre, self.apellido)
    

class Admin(Usuario):
    def superSaludo(self):
        print('Hola, me llamo,' , self.nombre, ' y soy administrador')

# usuario = Usuario('felipe', 'feliz')

# usuario.saludo()
# usuario.nombre = 'chanchito'
# usuario.saludo()
# # del usuario.nombre
# # del Usuario
# # print (usuario)

# admin = Admin('Super', 'Feliz')
# admin.saludo()
# admin.superSaludo()

# usuario.superSaludo()

class Animal:
    def __init__(self,nombre,onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola soy un gato extendido')

class Perros(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('instanciando un perro')

class Canario(Animal):
    tipo = 'canario'

gato = Gato('fluffy', 'maullido')
gato.saludo()

Perro = Perros('Fluffly', 'ladrido')
Perro.saludo()

Canario = Canario('pillin', 'silvido')
Canario.saludo()