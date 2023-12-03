import pymysql

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn

# Agregar artesano
def getComunaIdByName(comuna):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id FROM comuna WHERE nombre = %s", [comuna])
	id = cursor.fetchone()
	cursor.close()
	conn.close()
	return id

def postArtesano(comuna_id, descripcion_artesania, nombre, email, celular):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO artesano (comuna_id, descripcion_artesania, nombre, email, celular) VALUES (%s, %s, %s, %s, %s)", [comuna_id, descripcion_artesania, nombre, email, celular]) 
	conn.commit()
	cursor.close()
	conn.close()
	return 

def getArtesanoId(comuna_id, nombre, email, celular):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM artesano WHERE comuna_id = %s AND nombre = %s AND email = %s AND celular = %s", [comuna_id, nombre, email, celular]) 
    id = cursor.fetchone()
    cursor.close()
    conn.close()
    return id

def getTipoArtesaniaId(nombre):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id FROM tipo_artesania WHERE nombre = %s", [nombre]) 
	id = cursor.fetchone()
	cursor.close()
	conn.close()
	return id

def postArtesanoTipo(artesano_id, tipo_artesania_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO artesano_tipo (artesano_id, tipo_artesania_id) VALUES (%s, %s)", [artesano_id, tipo_artesania_id]) 
	conn.commit()
	cursor.close()
	conn.close()
	return 

def postFoto(ruta, nombre, artesano_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO foto (ruta_archivo, nombre_archivo, artesano_id) VALUES (%s, %s, %s)", [ruta, nombre, artesano_id]) 
	conn.commit()
	cursor.close()
	conn.close()
	return 



# Ver artesanos
def getArtesanos(n=0, limite=5):
	conn = get_conn() 
	cursor = conn.cursor()
	cursor.execute('SELECT id, nombre, celular, comuna_id FROM artesano LIMIT %s OFFSET %s', (limite, n))
	artesanos = cursor.fetchall()
	conn.close()
	return artesanos

def getArtesanosCount():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT COUNT(*) FROM artesano")
	n = cursor.fetchone()
	cursor.close()
	conn.close()
	return n

def getComunaById(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT nombre FROM comuna WHERE id = %s", [id])
	id = cursor.fetchone()
	cursor.close()
	conn.close()
	return id

def getArtesaniasByArtesano(artesano_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT nombre FROM tipo_artesania WHERE id IN (SELECT tipo_artesania_id FROM artesano_tipo WHERE artesano_id = %s)", [artesano_id])
	tipos = cursor.fetchall()
	cursor.close()
	conn.close()
	return tipos

def getFotosByArtesano(artesano_id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT ruta_archivo FROM foto WHERE artesano_id = %s", [artesano_id])
    fotos = [foto[0] for foto in cursor.fetchall()] 
    cursor.close()
    conn.close()
    return fotos



# Información artesano
def getArtesano(id):
    data = {}
    conn = get_conn() 
    cursor = conn.cursor()
    cursor.execute('SELECT id, comuna_id, descripcion_artesania, nombre, email, celular FROM artesano WHERE id = %s', (id,))
    result = cursor.fetchone()
    if result:
        data['id'], data['comuna_id'], data['descripcion_artesania'], data['nombre'], data['email'], data['celular'] = result
    if 'comuna_id' in data:
        cursor.execute('SELECT nombre FROM comuna WHERE id = %s', (data['comuna_id'],))
        comuna_name = cursor.fetchone()
        if comuna_name:
            data['comuna_nombre'] = comuna_name[0]
    if 'comuna_id' in data:
        cursor.execute('SELECT nombre FROM region WHERE id = (SELECT region_id FROM comuna WHERE id = %s)', (data['comuna_id'],))
        region_name = cursor.fetchone()
        if region_name:
            data['region_nombre'] = region_name[0]
    cursor.execute('SELECT ruta_archivo FROM foto WHERE artesano_id = %s', (id,))
    fotos = cursor.fetchall()
    if fotos:
        data['fotos'] = [foto[0] for foto in fotos]
    cursor.execute('SELECT nombre FROM tipo_artesania WHERE id IN (SELECT tipo_artesania_id FROM artesano_tipo WHERE artesano_id = %s)', (id,))
    tipos = cursor.fetchall()
    if tipos:
        data['tipos_artesania'] = [tipo[0] for tipo in tipos]
    conn.close()
    return data



# Agregar hincha
def postHincha(comuna_id, modo_transporte, nombre, email, celular, comentarios):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO hincha (comuna_id, modo_transporte, nombre, email, celular, comentarios) VALUES (%s, %s, %s, %s, %s, %s)", [comuna_id, modo_transporte, nombre, email, celular, comentarios]) 
	conn.commit()
	cursor.close()
	conn.close()
	return 

def getHinchaId(comuna_id, modo_transporte, nombre, email, celular, comentarios):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM hincha WHERE comuna_id = %s AND modo_transporte = %s AND nombre = %s AND email = %s AND celular = %s AND comentarios = %s", [comuna_id, modo_transporte, nombre, email, celular, comentarios]) 
    id = cursor.fetchone()
    cursor.close()
    conn.close()
    return id

def postDeporte(hincha_id, deporte_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO hincha_deporte (hincha_id, deporte_id) VALUES (%s, %s)", [hincha_id, deporte_id]) 
	conn.commit()
	cursor.close()
	conn.close()
	return 

def getDeporteId(nombre):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT id FROM deporte WHERE nombre = %s", [nombre]) 
	id = cursor.fetchone()
	cursor.close()
	conn.close()
	return id



# Ver hinchas
def getHinchas(n=0, limite=5):
	conn = get_conn() 
	cursor = conn.cursor()
	cursor.execute('SELECT id, nombre, celular, comuna_id, modo_transporte FROM hincha LIMIT %s OFFSET %s', (limite, n))
	hinchas = cursor.fetchall()
	conn.close()
	return hinchas

def getHinchasCount():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT COUNT(*) FROM hincha")
	n = cursor.fetchone()
	cursor.close()
	conn.close()
	return n

def getDeportesByHincha(id_hincha):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT nombre FROM deporte WHERE id IN (SELECT deporte_id FROM hincha_deporte WHERE hincha_id = %s)", [id_hincha])
	deportes = cursor.fetchall()
	cursor.close()
	conn.close()
	return deportes



# Información hincha
def getHincha(id):
    data = {}
    conn = get_conn() 
    cursor = conn.cursor()
    cursor.execute('SELECT id, comuna_id, modo_transporte, nombre, email, celular, comentarios FROM hincha WHERE id = %s', (id,))
    result = cursor.fetchone()
    if result:
        data['id'], data['comuna_id'], data['modo_transporte'], data['nombre'], data['email'], data['celular'], data['comentarios'] = result
    if 'comuna_id' in data:
        cursor.execute('SELECT nombre FROM comuna WHERE id = %s', (data['comuna_id'],))
        comuna_name = cursor.fetchone()
        if comuna_name:
            data['comuna_nombre'] = comuna_name[0]
    if 'comuna_id' in data:
        cursor.execute('SELECT nombre FROM region WHERE id = (SELECT region_id FROM comuna WHERE id = %s)', (data['comuna_id'],))
        region_name = cursor.fetchone()
        if region_name:
            data['region_nombre'] = region_name[0]
    cursor.execute('SELECT nombre FROM deporte WHERE id IN (SELECT deporte_id FROM hincha_deporte WHERE hincha_id = %s)', (id,))
    deportes = cursor.fetchall()
    if deportes:
        data['deportes'] = [deporte[0] for deporte in deportes]
    conn.close()
    return data



# Gráficos
def getDeportes():
	conn = get_conn() 
	cursor = conn.cursor()
	cursor.execute('SELECT id, nombre FROM deporte')
	deportes = cursor.fetchall()
	conn.close()
	return deportes

def getNumHinchasByDeporte(id_deporte):
	conn = get_conn() 
	cursor = conn.cursor()
	cursor.execute('SELECT COUNT(hincha_id) FROM hincha_deporte WHERE deporte_id = %s', (id_deporte,))
	hinchas = cursor.fetchone()
	conn.close()
	return hinchas

def getTiposArtesanias():
	conn = get_conn() 
	cursor = conn.cursor()
	cursor.execute('SELECT id, nombre FROM tipo_artesania')
	tipos = cursor.fetchall()
	conn.close()
	return tipos

def getNumArtesanosByTipoArtesania(id_artesania):
	conn = get_conn() 
	cursor = conn.cursor()
	cursor.execute('SELECT COUNT(artesano_id) FROM artesano_tipo WHERE tipo_artesania_id = %s', (id_artesania,))
	artesanos = cursor.fetchone()
	conn.close()
	return artesanos