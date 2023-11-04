import csv
import random

# de la lista de empresas sacamos una linea random y conseguimos los datos
empresas = []
with open('empresas.csv', mode='r', newline='', encoding='utf-8') as empresas_file:
    reader = csv.reader(empresas_file, delimiter=';')
    for row in reader:
        empresas.append(row)

empresas_lista = []
for i in range (100):
    empresa_random = random.choice(empresas)
    empresa = {
        "razon_social": empresa_random[2],
        "rut": empresa_random[1]
        #"nombre": es necesario el nombre? al final la razon social es el nombre legal
    }
    empresas_lista.append(empresa)

with open("lista_clientes.csv", mode="w", newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=empresas_lista[0].keys())
    writer.writeheader()
    writer.writerows(empresas_lista)