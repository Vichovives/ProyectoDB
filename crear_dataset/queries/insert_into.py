import psycopg2

def insert_into(cursor, table_name, values):
    try:
        query = f"INSERT INTO {table_name} ("
        query +=  f"{','.join(values.keys())})"
        query += f"VALUES ({', '.join(['%s' for _ in values.values()])});"

        cursor.execute(query, tuple(values.values()))
        cursor.connection.commit()

    except psycopg2.Error as err:
        print(f"Error al insertar datos en la tabla '{table_name}': {err}")

