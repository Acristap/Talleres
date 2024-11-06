# estructuras de {llave: valor}

my_diccionario = {
    "nombre": "Yurley",
    "apellido": "Sanchez",
    "edad": 35,
}

print('my_diccionario', my_diccionario)
print(my_diccionario['edad'])
print(my_diccionario.get('edad'))

print(my_diccionario.get('edadd'))
#print(my_diccionario['edadd'])
print(my_diccionario.keys())
print(my_diccionario.values())
print(my_diccionario.items())