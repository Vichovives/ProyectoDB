from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from utils.validations import validadorArtesano, validadorHincha
from database import db
import hashlib
import filetype
import os
from werkzeug.utils import secure_filename
from flask_paginate import Pagination
from flask_cors import cross_origin

def parser(texto):
    texto_sin_comillas = texto.replace("'", "").replace('"', '')
    texto_sin_parentesis = texto_sin_comillas.replace("(", "").replace(")", "")    
    return texto_sin_parentesis

def tuplaACadenaComunas(tupla):
    elementos_convertidos = [str(elemento) for elemento in tupla]
    cadena_resultante = ", ".join(elementos_convertidos)
    return cadena_resultante

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/agregar-artesano", methods=("GET", "POST"))
def agregarArtesano():
    error = None
    if request.method == "POST":
        nombre = request.form['nombre']
        correo = request.form['correo']
        numero = request.form['numero']
        descripcion = request.form.get('descripcion', None) 
        region = request.form.get('region', None)  
        comuna = request.form.get('comuna', None)  
        fotos = request.files.getlist('fotos')
        estadoCheckboxes = request.form.getlist('tipo_artesania')
        if validadorArtesano(nombre, correo, numero, region, comuna, estadoCheckboxes, fotos , descripcion):
            id_comuna = db.getComunaIdByName(comuna)
            db.postArtesano(id_comuna, descripcion, nombre, correo, numero)
            idArtesano = db.getArtesanoId(id_comuna, nombre, correo, numero)
            for tipo in estadoCheckboxes:
                idTipo = db.getTipoArtesaniaId(tipo)
                db.postArtesanoTipo(idArtesano, idTipo)
            for foto in fotos:
                _filename = hashlib.sha256(
                    secure_filename(foto.filename)
                    .encode("utf-8") 
                    ).hexdigest()
                _extension = filetype.guess(foto).extension
                imgName = f"{_filename}.{_extension}"
                foto.save(os.path.join(app.config["UPLOAD_FOLDER"], imgName))
                ruta = 'uploads/' + imgName
                db.postFoto(ruta, imgName, idArtesano)
            return redirect(url_for('index'))
        else:
            error = "Los datos del artesano no son válidos. Por favor, verifica e inténtelo de nuevo."
    return render_template("agregarArtesano.html", error=error)

@app.route("/agregar-hincha", methods=("GET", "POST"))
def agregarHincha():
    error = None
    if request.method == "POST":
        nombre = request.form['nombre']
        correo = request.form['correo']
        numero = request.form['numero']
        region = request.form.get('region', None)  
        comuna = request.form.get('comuna', None)
        modoTransporte = request.form['transporte']
        comentarios = request.form.get('comentarios', None) 
        estadoCheckboxes = request.form.getlist('deporte')
        if validadorHincha(nombre, correo, numero, estadoCheckboxes, region, comuna, modoTransporte, comentarios):
            id_comuna = db.getComunaIdByName(comuna)
            db.postHincha(id_comuna, modoTransporte, nombre, correo, numero, comentarios)
            idHincha = db.getHinchaId(id_comuna, modoTransporte, nombre, correo, numero, comentarios)
            for deporte in estadoCheckboxes:
                idDeporte = db.getDeporteId(deporte)
                db.postDeporte(idHincha, idDeporte)
            return redirect(url_for('index'))
        else:
            error = "Los datos del hincha no son válidos. Por favor, verifica e inténtelo de nuevo."
    return render_template("agregarHincha.html", error=error)

@app.route("/ver-artesanos", methods=["GET"])
@app.route("/ver-artesanos/page/<int:page>", methods=["GET"])
def verArtesanos(page=1):
    PER_PAGE = 5
    n = (page - 1) * PER_PAGE
    artesanos = db.getArtesanos(n, PER_PAGE)
    pctotal = db.getArtesanosCount()
    total = pctotal[0]
    filasTabla = []
    for artesano in artesanos:
        pccomuna = db.getComunaById(artesano[3])
        artesanias = db.getArtesaniasByArtesano(artesano[0])
        partesanias = [artesania[0] for artesania in artesanias]
        fotos = db.getFotosByArtesano(artesano[0])
        fila = [artesano[1], artesano[2], pccomuna[0], partesanias, fotos, artesano[0]]
        filasTabla.append(fila)
    pagination = Pagination(page=page,
                            per_page=PER_PAGE,
                            total=total,
                            css_framework='bootstrap4')
    return render_template("verArtesanos.html", artesanos=filasTabla, pagination=pagination)

@app.route("/ver-hincha", methods=["GET"])
@app.route("/ver-hincha/page/<int:page>", methods=["GET"])
def verHinchas(page=1):
    PER_PAGE = 5
    n = (page - 1) * PER_PAGE
    hinchas = db.getHinchas(n, PER_PAGE)
    pctotal = db.getHinchasCount()
    total = pctotal[0]
    filasTabla = []
    for hincha in hinchas:
        pccomuna = db.getComunaById(hincha[3])
        deportes = db.getDeportesByHincha(hincha[0])
        pcdeportes = [deporte[0] for deporte in deportes]
        fila = [hincha[1], pccomuna[0], pcdeportes, hincha[4], hincha[2], hincha[0]]
        filasTabla.append(fila)
    pagination = Pagination(page=page,
                            per_page=PER_PAGE,
                            total=total,
                            css_framework='bootstrap4')

    return render_template("verHinchas.html", hinchas=filasTabla, pagination=pagination)

@app.route("/informacion-artesano/<int:id>", methods=["GET"])
def informacionArtesano(id):
    artesano = db.getArtesano(id)
    info = {
    "nombre": artesano["nombre"],
    "email": artesano["email"],
    "celular": artesano["celular"],
    "comuna": artesano["comuna_nombre"],  
    "region": artesano["region_nombre"],
    "descripcion": artesano["descripcion_artesania"],
    "tipo_artesania": ", ".join([tipo for tipo in artesano["tipos_artesania"]]),
    "fotos": artesano["fotos"]
    }
    return render_template("informacionArtesano.html", artesano=info)

@app.route("/informacion-hincha/<int:id>", methods=["GET"])
def informacionHincha(id):
    hincha = db.getHincha(id)
    info = {
    "nombre": hincha["nombre"],
    "email": hincha["email"],
    "celular": hincha["celular"],
    "comuna": hincha["comuna_nombre"],  
    "region": hincha["region_nombre"],
    "comentarios": hincha["comentarios"],
    "deportes": ", ".join([deporte for deporte in hincha["deportes"]]),
    "modo_transporte": hincha["modo_transporte"]
    }
    return render_template("informacionHincha.html", hincha=info)

@app.route("/stats", methods=["GET"])
def stats():
    return render_template("stats.html")

@app.route("/get_stats_data", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def get_stats_data():
    dataArtesanos = {}
    tiposArtesanias = db.getTiposArtesanias()
    for tipo in tiposArtesanias:
        dataArtesanos[tipo[1]] = db.getNumArtesanosByTipoArtesania(tipo[0])[0]
    
    dataHinchas = {}
    deportes = db.getDeportes()
    for deporte in deportes:
        dataHinchas[deporte[1]] = db.getNumHinchasByDeporte(deporte[0])[0]
    data = {
        "artesanos": dataArtesanos,
        "hinchas": dataHinchas
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)