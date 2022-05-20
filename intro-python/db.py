import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='prueba',
)

cursor = midb.cursor()

# listar datos
""" cursor.execute('select * from usuario')
resultado = cursor.fetchone()
print(resultado) """

cursor.execute('select * from usuario limit 1')
resultado = cursor.fetchone()
print(resultado)


# ver definiciones de tablas
""" cursor.execute('show create table usuario') """

""" 
sql = 'insert into usuario (email, username, edad) values (%s, %s, %s)'
values = ('micorreo@correo.com', 'nombreusuario', 45)
"""

# actualiza datos 
""" 
sql = 'update usuario set email = %s where id =%s'
values = ('nachi@correo.com.ar', 2)
cursor.execute(sql, values)

midb.commit()
 """

#print(cursor.rowcount)

# Eliminar da tos
""" 
sql = 'delete from usuario where id = %s'
values = (2,)
cursor.execute(sql, values)
midb.commit()
 """


