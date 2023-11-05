import csv
import random
import psycopg2
import psycopg2.extras

from datetime import datetime

from database import initializers

from queries import create_table
from queries import insert_into

# Nos conectamos a la db
conn = initializers.DBInstance()
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

columns = [
    "factura_rut_receptor varchar(20) not null",
    "factura_razon_social varchar(120) not null",
    "factura_folio integer primary key not null unique",
    "factura_fecha_emision timestamp not null",
    "factura_monto bigint not null",
    "factura_estado_sii varchar(40) not null"
]
create_table.create_table(cursor, "facturas", columns)

# de las empresas sacamos una linea random y conseguimos los datos
empresas = []
with open('empresas.csv', mode='r', newline='', encoding='utf-8') as empresas_file:
    reader = csv.reader(empresas_file, delimiter=';')
    for row in reader:
        empresas.append(row)




# Generamos las facturas ficticias

# puse 10000, porque esas son las tuplas, podemos cambiarla segun lo que necesitemos
# rango de fecha de las facturas
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 11, 3)

facturas = []
for i in range(20):
    empresa = random.choice(empresas)
    fecha_emision = start_date + (end_date - start_date) * random.random()
    fecha_emision_str = fecha_emision.strftime('%Y-%m-%d %H:%M:%S')  # Formatear la fecha sin milisegundos
    factura = {
        "factura_folio": i + 1,
        "factura_rut_receptor": empresa[1],
        "factura_razon_social": empresa[2],
        "factura_monto": random.randint(40000,1000000),
        "factura_fecha_emision": fecha_emision_str,
        "factura_estado_sii": "Documento Aceptado",
    }
    insert_into.insert_into(cursor, "facturas", factura)
    print(f"Registro {i} creado")
    



# Escribir el archivo csv
# Puede que no sea necesario escribirlo en csv, podriamos desde aqui insertar a la base de datos, 
# pero puede ayudar a mantener consistencia con los datos

with open("lista_facturas.csv", mode="w", newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=facturas[0].keys())
    writer.writeheader()
    writer.writerows(facturas)