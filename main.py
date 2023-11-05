# Subir a DB
table_name = "operacions"

values = {
        "operacion_cliente": 1,
        "operacion_cantidad_facturas": 2,
        "operacion_gasto_operacional": 3,
        "operacion_gasto_administrativo": 4,
        "operacion_monto": 5,
        "operacion_interes": 6,
        "operacion_mora": 7,
        "operacion_fecha_curse": 8,
        "operacion_fecha_vencimiento": 9,
        "operacion_fecha_pago": 10
    }

#query = f"INSERT INTO {table_name} ("
#query +=  f"{','.join(values.keys())})"
#query += f"VALUES ({', '.join(['%s' for _ in values.values()])});"

query=f"INSERT INTO {table_name} ({', '.join(values.keys())}) VALUES ({', '.join(['%s' for _ in values.values()])});"

print(query)