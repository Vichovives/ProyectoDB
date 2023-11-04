import csv
import random
import string
from funciones_auxiliares import crear_rut as cr
from funciones_auxiliares import crear_telefono as ct
from funciones_auxiliares import crear_email as ce
from funciones_auxiliares import crear_password as cp

usuarios_lista = []
with open('personas.csv', mode='r', newline='', encoding='utf-8') as personas_file:
    reader = csv.reader(personas_file, delimiter=';')
    for row in reader:
        usuarios_lista.append(row)



usuarios = []
for i in range(100):
    datos = random.choice(usuarios_lista)
    usuario = {
        "rut": cr.generar_rut_aleatorio(),
        "apellido": datos[2],
        "nombre":datos[1],
        "telefono": ct.generar_numero_telefonico_chileno(),
        "email": ce.creardor_email(datos[1], datos[2]),
        "password": cp.generar_contrasena()
    }
    usuarios.append(usuario)

with open("lista_usuarios.csv", mode="w", newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=usuarios[0].keys())
    writer.writeheader()
    writer.writerows(usuarios)   
    