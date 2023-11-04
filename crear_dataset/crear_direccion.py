import csv
import random
from random_address import real_random_address


regiones = []
with open('comuna_region.csv', mode='r', newline='', encoding='utf-8') as regiones_file:
    reader = csv.reader(regiones_file, delimiter=',')
    for row in reader:
        regiones.append(row)


direcciones = []
for i in range(100):
    datos = random.choice(regiones)
    calle = real_random_address()
    dirrecion = { 
        "calle": calle.get('address1'),
        "comuna": datos[2],
        "ciudad": datos[0]     
    }
    direcciones.append(dirrecion)

with open("lista_direcciones.csv", mode="w", newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=direcciones[0].keys())
    writer.writeheader()
    writer.writerows(direcciones)