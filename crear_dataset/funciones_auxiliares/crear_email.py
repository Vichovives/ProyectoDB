def creardor_email(nombre, apellido):
    nombre_minuscula = nombre.lower()
    apellido_minuscula = apellido.lower()
    if ' ' in nombre_minuscula:
        nombre_minuscula = '.'.join(nombre_minuscula.split())
    if ' ' in apellido_minuscula:
        apellido_minuscula = '.'.join(apellido_minuscula.split())
    return nombre_minuscula + '.' + apellido_minuscula + '@gmail.cl' # puse dominio gmail, pero si queremos podriamos poner que el nombre de la empresa sea el dominio