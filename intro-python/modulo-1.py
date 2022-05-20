import modulos as xs
from camelcase import CamelCase


print(xs.mascotas)
xs.saludo('Ignacio') 

c = CamelCase()
s = 'esta oracion necesita CamelCase!'


camelcased = c.hump(s)
print (camelcased)