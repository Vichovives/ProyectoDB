import re
import filetype

# Nombre
def validadorNombre(nombre):
    if (3 <= len(nombre) <= 80) and re.match(r'^[A-Za-z\s]+$', nombre):
        return True
    else:
        return False

# Correo
def validadorCorreo(correo):
    if re.match(r"[^@]+@[^@]+\.[^@]+", correo):
        return True
    else:
        return False

# Número
def validadorNumero(numero):
    patron_numero = r"^\+(?:\d{1,3})?(?:\s*-\s*\d{1,})+$"
    if not numero or len(numero) > 15:
        if not re.match(patron_numero, numero):
            return False    
    return True

# Región
def validadorRegion(region):
    if not region:
        return False
    else:
        return True

# Comuna
def validadorComuna(comuna):
    if not comuna:
        return False
    else:
        return True

# Tipo de artesanía
def validadorTipoArtesania(tipos):
    return 1 <= len(tipos) <= 3

# Fotos
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}
def validadorFotos(listaFotos):
    def validarFoto(foto):
        ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
        ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}
        if foto is None:
            return False
        if foto.filename == "":
            return False
        ftype_guess = filetype.guess(foto)
        if ftype_guess.extension not in ALLOWED_EXTENSIONS:
            return False
        if ftype_guess.mime not in ALLOWED_MIMETYPES:
            return False
        return True
    for foto in listaFotos:
        if not validarFoto(foto):
            return False
    return True

# Descripción
def validadorDescripcion(descripcion):
    patronesMaliciosos = re.compile(r"<[^>]+>|&[^;]+;")
    if re.search(patronesMaliciosos, descripcion):
        return False
    return True

# Artesano
def validadorArtesano(nombre, correo, numero, region, comuna, checkboxes, fotos, descripcion):
    valid_nombre = validadorNombre(nombre)
    valid_correo = validadorCorreo(correo)
    valid_numero = validadorNumero(numero)
    valid_region = validadorRegion(region)
    valid_comuna = validadorComuna(comuna)
    valid_tipo_artesania = validadorTipoArtesania(checkboxes)
    valid_fotos = validadorFotos(fotos)
    valid_descripcion = validadorDescripcion(descripcion)
    if not valid_nombre:
        print(nombre)
    if not valid_correo:
        print(correo)
    if not valid_numero:
        print(numero)
    if not valid_region:
        print(region)
    if not valid_comuna:
        print(comuna)
    if not valid_tipo_artesania:
        print(checkboxes)
    if not valid_fotos:
        print(fotos)
    if not valid_descripcion:
        print(descripcion)
    return valid_nombre and valid_correo and valid_numero and valid_region and valid_comuna and valid_tipo_artesania and valid_fotos and valid_descripcion


# Deporte(s) de interés
def validadorDeportes(deportes):
    return 1 <= len(deportes) <= 3

# Modo de Transporte
def validadorTransporte(transporte):
    return transporte in ["particular", "locomoción pública"]

# Comentarios 
def validadorComentarios(comentarios):
    if len(comentarios) > 80:
        return False
    if re.search('<[^<]+?>', comentarios):
        return False
    return True

# Hincha
def validadorHincha(nombre, correo, numero, deportes, region, comuna, transporte, comentarios):
    valid_nombre = validadorNombre(nombre)
    valid_correo = validadorCorreo(correo)
    valid_numero = validadorNumero(numero)
    valid_deportes = validadorDeportes(deportes)
    valid_region = validadorRegion(region)
    valid_comuna = validadorComuna(comuna)
    valid_transporte = validadorTransporte(transporte)
    valid_comentarios = validadorComentarios(comentarios)
    if not valid_nombre:
        print(nombre)
    if not valid_correo:
        print(correo)
    if not valid_numero:
        print(numero)
    if not valid_deportes:
        print(deportes)
    if not valid_region:
        print(region)
    if not valid_comuna:
        print(comuna)
    if not valid_transporte:
        print(transporte)
    if not valid_comentarios:
        print(comentarios)
    return valid_nombre and valid_correo and valid_numero and valid_deportes and valid_region and valid_comuna and valid_transporte and valid_comentarios


