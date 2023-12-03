import random

def generar_numero_telefonico_chileno():
    numero = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return f"+569{numero}"
