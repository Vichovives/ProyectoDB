def create_table(cursor, name_table, columns):
    try:
        # Generar la consulta SQL para crear la tabla
        query = f"CREATE TABLE {name_table} ("
        query += ', '.join(columns)
        query += ");"

        # Ejecutar la consulta SQL
        cursor.execute(query)

        # Confirmar los cambios en la base de datos
        cursor.connection.commit()

        print(f"Tabla '{name_table}' creada exitosamente.")
    except psycopg2.Error as err:
        print(f"Error al crear la tabla '{name_table}': {err}")