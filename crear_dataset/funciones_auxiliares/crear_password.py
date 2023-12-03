import random
import string

def generar_contrasena():
    longitud = random.randint(10, 15)  # Longitud entre 10 y 15
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena