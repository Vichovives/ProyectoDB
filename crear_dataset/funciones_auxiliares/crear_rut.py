import random

def generar_rut_aleatorio():
    rut = str(random.randint(1000000, 30000000))  # Genera el número sin el dígito verificador
    return rut + '-' + str(random.randint(0, 9))  # a;adimos digito verificador