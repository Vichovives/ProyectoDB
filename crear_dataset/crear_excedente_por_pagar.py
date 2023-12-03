import csv
import random
import string
import datetime

import psycopg2
import psycopg2.extras

from database import initializers

from queries import create_table
from queries import insert_into

from funciones_auxiliares import crear_gasto_administrativo as cga
from funciones_auxiliares import crear_gasto_operacion as cgo
from funciones_auxiliares import crear_fecha_curse as cfc
from funciones_auxiliares import crear_fecha_vencimiento as cfv
from funciones_auxiliares import crear_fecha_pago as cfp
from funciones_auxiliares import crear_mora as cm
from funciones_auxiliares import crear_porcentaje_anticipo as cpa


# Nos conectamos a la db
conn = initializers.DBInstance()
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

columns = [
    "excedente_por_pagar_deudor varchar(120) NOT NULL",
    "excedente_por_pagar_numero_dcto integer primary key NOT NULL unique",
    "excedente_por_pagar_fecha_vencimiento timestamp NOT NULL",
    "excedente_por_pagar_valor_dcto bigint NOT NULL",
    "excedente_por_pagar_intereses_mora bigint NOT NULL",
    "excedente_por_pagar_gastos bigint NOT NULL",
    "excedente_por_pagar_saldo_x_pagar bigint NOT NULL",
    "excedente_por_pagar_porcentaje_anticipo real NOT NULL",
    "excedente_por_pagar_monto_anticipo bigint NOT NULL"
]

create_table.create_table(cursor, "excedente_por_pagars", columns)

ROWS = 7

empresas = []
with open('empresas.csv', mode='r', newline='', encoding='utf-8') as empresas_file:
    reader = csv.reader(empresas_file, delimiter=';')
    for row in reader:
        empresas.append(row)

empresas_lista = []
for i in range (ROWS):
    empresa_random = random.choice(empresas)
    empresas_lista.append(empresa_random)

#excedente_list = []
for i in range(ROWS):
    valor_dcto = random.randint(40000,1000000)
    fecha_curse = cfc.crear_fecha_curse(datetime.datetime(2023,8,5), datetime.datetime(2023,11,5))
    fecha_vencimiento = cfv.crear_fecha_vencimiento(fecha_curse)
    fecha_pago = cfp.crear_fecha_pago(fecha_curse, fecha_vencimiento)
    interes = round(random.uniform(0.03, 0.009), 6)
    porcentaje_anticipo = cpa.crear_porcentaje_anticipo()
    excedente = valor_dcto * (1-porcentaje_anticipo)
    dif_precio = cm.crear_mora(valor_dcto*porcentaje_anticipo, fecha_vencimiento, fecha_pago)
    dev_cliente = excedente - dif_precio
    excedente_por_pagar = {
        "excedente_por_pagar_deudor": empresas_lista[i][2],
        "excedente_por_pagar_numero_dcto": (i+1)*16,
        "excedente_por_pagar_fecha_vencimiento": fecha_vencimiento,
        "excedente_por_pagar_valor_dcto": valor_dcto,
        "excedente_por_pagar_intereses_mora": dif_precio,
        "excedente_por_pagar_gastos": 0,
        "excedente_por_pagar_saldo_x_pagar": dif_precio,
        "excedente_por_pagar_porcentaje_anticipo": porcentaje_anticipo,
        "excedente_por_pagar_monto_anticipo": valor_dcto * porcentaje_anticipo,
    }
    #excedente_list.append(excedente_por_pagar)
    insert_into.insert_into(cursor, "excedente_por_pagars", excedente_por_pagar)
    print(f"Registro {i} creado")

"""

with open("excedente_por_pagar.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=excedente_list[0].keys())
    writer.writeheader()
    writer.writerows(excedente_list)

"""