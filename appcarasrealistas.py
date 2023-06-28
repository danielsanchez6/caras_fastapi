from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from flask_sqlalchemy import SQLAlchemy
import shutil
import datetime
import time
import os
import signal
import sys
import subprocess
from subprocess import Popen


import plotly.express as px

from fpdf import FPDF
from PIL import Image




# definicion plantilla pdf ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



class PDF(FPDF):
    # definir el header del documento.
    def header(self):
        self.image('static/img/indice2.png',10,10,30)

        self.image('static/img/indice3.png',45,13,50)


        #self.set_font('helvetica', 'B', 20)
        #self.cell(0,10,'Tittle', border=False, ln=1, align='C')


        self.image('static/img/indice1.png',100,8,50)

        self.image('static/img/indice.png',150,12,50)
        
        #salto de linea
        self.ln(20)

    def footer(self):
        # se define la posicion del footer
        self.set_y(-15)
        # se define la fuente del footer
        self.set_font('helvetica', 'I', 10)
        # Color de texto en gris
        self.set_text_color(128)
        # se define el texto del footer (en este caso el numero de pagina)
        page = 'Página: ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')







# fin definicion plantilla pdf ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# Configuracion flask ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    
    appcarasrealistas = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

else:
    appcarasrealistas = Flask(__name__)
    



#creacion de una clave secreta
appcarasrealistas.secret_key = 'clave_secreta_flask'

# configurar la ruta de las bases de datos
appcarasrealistas.config['SQLALCHEMY_BINDS'] = {'datosappcarasrealistas': 'sqlite:///database/dbappcarasrealistas.db'}
appcarasrealistas.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(appcarasrealistas)

# crear las tablas y las columnas de la base de datos
# para añadir el modelo a la base de datos desde terminal:
# python
# from appcarasrealistas import db
# db.create_all(bind=['datosappcarasrealistas'])
# exit()



# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Tabla datos formulario de registro para participante

class Formularioregistro(db.Model):
    __bind_key__ = 'datosappcarasrealistas'
    # identificador del participante
    idparticipante = db.Column(db.Integer, primary_key=True)

    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    # numero historial clinico del participante
    nhcparticipante = db.Column(db.Text)
    
    # datos sociodemograficos del participante
    edad = db.Column(db.Text)
    genero = db.Column(db.Text)
    textogenero = db.Column(db.Text)
    etnia = db.Column(db.Text)
    estadocivil = db.Column(db.Text)
    provinciaresidencia = db.Column(db.Text)
    textoprovinciaresidencia = db.Column(db.Text)
    residencia = db.Column(db.Text)
    estudios = db.Column(db.Text)
    situacionprofesional = db.Column(db.Text)
    textosituacionprofesional = db.Column(db.Text)
    profesion = db.Column(db.Text)
    


# Tabla datos formulario secundario para participante

class Formularioantecedentes(db.Model):
    __bind_key__ = 'datosappcarasrealistas'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idparticipante = db.Column(db.Text)
    nhcparticipante = db.Column(db.Text)

    tipoparticipante = db.Column(db.Text)
    estadoparticipante = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)
    
    # datos antecedentes personales somáticos para participante
    antecedentespersonalessomaticos = db.Column(db.Text)
    
    # datos antecedentes personales psiquiatricos para participante
    diagnosticodms5 = db.Column(db.Text)
    faseenfermedadactual = db.Column(db.Text)
    edadiniciosintomatologia = db.Column(db.Text)
    anosevolucionenfermedad = db.Column(db.Text)
    numerodescompensaciones = db.Column(db.Text)
    numerodescompensaciones6meses = db.Column(db.Text)
    numeroingresos = db.Column(db.Text)
    numeroingresos6meses = db.Column(db.Text)
    tratamientopsicofarmacologico = db.Column(db.Text)
    tratamientopsicofarmacologico = db.Column(db.Text)
    tratamientomedicoactual = db.Column(db.Text)
    antecedentespersonalestoxicos1 = db.Column(db.Text)
    antecedentespersonalestoxicos8 = db.Column(db.Text)
    antecedentespersonalestoxicos2 = db.Column(db.Text)
    antecedentespersonalestoxicos3 = db.Column(db.Text)
    antecedentespersonalestoxicos4 = db.Column(db.Text)
    antecedentespersonalestoxicos5 = db.Column(db.Text)
    antecedentespersonalestoxicos6 = db.Column(db.Text)
    antecedentespersonalestoxicos7 = db.Column(db.Text)
    textoantecedentespersonalestoxicos = db.Column(db.Text)
    criteriosabuso = db.Column(db.Text)
    antecedentesfamiliarespsiquiatricos = db.Column(db.Text)


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Tabla datos participante

class Escalapanas(db.Model):
    __bind_key__ = 'datosappcarasrealistas'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idparticipante = db.Column(db.Text)
    nhcparticipante = db.Column(db.Text)

    tipoparticipante = db.Column(db.Text)
    estadoparticipante = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalapanas1 = db.Column(db.Text)
    escalapanas2 = db.Column(db.Text)
    escalapanas3 = db.Column(db.Text)
    escalapanas4 = db.Column(db.Text)
    escalapanas5 = db.Column(db.Text)
    escalapanas6 = db.Column(db.Text)
    escalapanas7 = db.Column(db.Text)
    escalapanas8 = db.Column(db.Text)
    escalapanas9 = db.Column(db.Text)
    escalapanas10 = db.Column(db.Text)
    escalapanas11 = db.Column(db.Text)
    escalapanas12 = db.Column(db.Text)
    escalapanas13 = db.Column(db.Text)
    escalapanas14 = db.Column(db.Text)
    escalapanas15 = db.Column(db.Text)
    escalapanas16 = db.Column(db.Text)
    escalapanas17 = db.Column(db.Text)
    escalapanas18 = db.Column(db.Text)
    escalapanas19 = db.Column(db.Text)
    escalapanas20 = db.Column(db.Text)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Appcaraspantalla(db.Model):
    __bind_key__ = 'datosappcarasrealistas'
    idnumericoappcaras = db.Column(db.Integer, primary_key=True)

    # datos fijos en cada fila appcaras
    idnumericoparticipante = db.Column(db.Text)
    nhcparticipante = db.Column(db.Text)

    # datos variables en cada fila appcaras

    horainiciocara = db.Column(db.Text)

    respuestacorrecta = db.Column(db.Text)
    respuestacorrectafiltrada = db.Column(db.Text)
    respuestausuario = db.Column(db.Text)
    acierto = db.Column(db.Text)
    tiemporesponder = db.Column(db.Text)
    camara = db.Column(db.Text)
    movimiento = db.Column(db.Text)
    hmd = db.Column(db.Text)
    coloravatar = db.Column(db.Text)
    tiempofinal = db.Column(db.Text)
    ordenaparicion = db.Column(db.Text)
    generoavatar = db.Column(db.Text)
    etniaavatar = db.Column(db.Text)
    
    

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Cuestionarioavatares(db.Model):
    __bind_key__ = 'datosappcarasrealistas'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idparticipante = db.Column(db.Text)
    nhcparticipante = db.Column(db.Text)

    tipoparticipante = db.Column(db.Text)
    estadoparticipante = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    cuestionarioavatares1 = db.Column(db.Text)
    cuestionarioavatares2 = db.Column(db.Text)
    cuestionarioavatares3 = db.Column(db.Text)
    cuestionarioavatares4 = db.Column(db.Text)
    cuestionarioavatares5_1 = db.Column(db.Text)
    cuestionarioavatares5_2 = db.Column(db.Text)
    cuestionarioavatares5_3 = db.Column(db.Text)
    cuestionarioavatares6 = db.Column(db.Text)
    cuestionarioavatares7 = db.Column(db.Text)
    cuestionarioavatares8 = db.Column(db.Text)
    cuestionarioavatares9 = db.Column(db.Text)


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# funciones ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# funciones para iniciar los formularios con los valores por defecto, para que se muestren bien los placeholders del html
def inicioformularioregistro(nombretablabd):
    formulario = nombretablabd(nhcparticipante ="", edad ="", textogenero ="", textoprovinciaresidencia ="", textosituacionprofesional ="", profesion ="")
    return formulario



# funcion get en sqlalchemy
def getparticipanteporid(nombretablabd, idparticipante):
    datoparticipante = nombretablabd.query.get(idparticipante)
    return datoparticipante



# funcion para crear el participante en cada escala
def crearparticipanteescala(nombretablabd, idparticipante, nhcparticipante, fechacreacion):

    if (nombretablabd == Formularioantecedentes):
        escala = nombretablabd(idparticipante = idparticipante, nhcparticipante = nhcparticipante, tipoparticipante="control", estadoparticipante="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", antecedentespersonalessomaticos="", diagnosticodms5="", edadiniciosintomatologia="", anosevolucionenfermedad="", numerodescompensaciones="", numeroingresos="", numerodescompensaciones6meses="", tratamientopsicofarmacologico="", tratamientomedicoactual="", antecedentesfamiliarespsiquiatricos="", textoantecedentespersonalestoxicos="", numeroingresos6meses="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalapanas):
        escala = nombretablabd(idparticipante = idparticipante, nhcparticipante = nhcparticipante, tipoparticipante="control", estadoparticipante="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala
    
    if (nombretablabd == Cuestionarioavatares):
        escala = nombretablabd(idparticipante = idparticipante, nhcparticipante = nhcparticipante, tipoparticipante="control", estadoparticipante="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", cuestionarioavatares9="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    return inicio



# funcion para modificar los nhc de los formularios secundarios y de las escalas
def modificarnhc(nombretablabd, idparticipante, nhcantiguo, nhcnuevo, fechacreacion):
    formulario = nombretablabd.query.filter_by(fechacreacion = fechacreacion).filter_by(idparticipante = idparticipante).filter_by(nhcparticipante = nhcantiguo).all()
    for n in formulario:
        n.nhcparticipante = nhcnuevo
        db.session.add(n)
        db.session.commit()



# funcion para modificar los nhc de los formularios appcaras
def modificarnhccaras(nombretablabd, idparticipante, nhcantiguo, nhcnuevo):
    formulario = nombretablabd.query.filter_by(idnumericoparticipante = idparticipante).filter_by(nhcparticipante = nhcantiguo).all()
    for n in formulario:
        n.nhcparticipante = nhcnuevo
        db.session.add(n)
        db.session.commit()



# funcion para buscar el primer registro el participante en cada escala
def buscarfirstparticipante(nombretablabd, idparticipante, nhcparticipante, fechacreacion):
    buscarfirst = nombretablabd.query.filter_by(fechacreacion = fechacreacion).filter_by(idparticipante = idparticipante).filter_by(nhcparticipante = nhcparticipante).first()
    return buscarfirst



# funcion para buscar el primer registro el participante en cada escala
def buscarfirstparticipanteappcaras(nombretablabd, idparticipante, nhcparticipante):
    buscarfirst = nombretablabd.query.filter_by(idnumericoparticipante = idparticipante).filter_by(nhcparticipante = nhcparticipante).first()
    return buscarfirst


# funcion para buscar el primer registro el participante en cada escala
def buscarallparticipanteappcaras(nombretablabd, idparticipante, nhcparticipante):
    buscarall = nombretablabd.query.filter_by(idnumericoparticipante = idparticipante).filter_by(nhcparticipante = nhcparticipante).all()
    return buscarall


# funcion para buscar el primer registro el participante en cada escala
def buscarallaciertosparticipanteappcaras(nombretablabd, idparticipante, nhcparticipante, emocion):
    #buscarallaciertos = nombretablabd.query.filter_by(idnumericoparticipante = idparticipante).filter_by(nhcparticipante = nhcparticipante).filter_by(respuestacorrecta = emocion).filter_by(acierto = "1").all()
    buscarallaciertos = nombretablabd.query.filter_by(idnumericoparticipante = idparticipante).filter_by(nhcparticipante = nhcparticipante).filter_by(respuestacorrectafiltrada = emocion).filter_by(acierto = "1").all()
    return buscarallaciertos





# funcion para borrar el participante en los formularios secundarios y en las escalas
def borrarescala(nombretablabd, idparticipante, nhcparticipante, fechacreacion):
    formulario = nombretablabd.query.filter_by(fechacreacion = fechacreacion).filter_by(nhcparticipante = nhcparticipante).filter_by(idparticipante = idparticipante).all()
    for n in formulario:
        db.session.delete(n)
        db.session.commit()

def borrarappcaras(nombretablabd, idparticipante, nhcparticipante):
    borrarappcaras = nombretablabd.query.filter_by(nhcparticipante=nhcparticipante).filter_by(idnumericoparticipante=idparticipante).all()
    for n in borrarappcaras:
        db.session.delete(n)
        db.session.commit()



# funcion para obtener lista de todos los nhc del programa
def nhclistatotal(database1):
    nhclista1 = [database1.nhcparticipante for database1 in database1.query.all()]
    nhclistasuma = nhclista1
    return nhclistasuma


# # funcion para obtener lista de todos los nhc del programa sin el nhc del participante
# def nhclistasinid(nombretablabd, idparticipante, database1):
#     nhclista1 = [database1.nhcparticipante for database1 in database1.query.all()]
#     nhclistasuma = nhclista1
    
#     datosparticipante = nombretablabd.query.get(idparticipante)
    
#     nhceliminar = datosparticipante.nhcparticipante
#     nhclistalimpio = list(filter((nhceliminar).__ne__, nhclistasuma))
    
#     return nhclistalimpio


# funcion para obtener lista de todos los nhc del programa sin el nhc del participante
def nhclistasinid(nombretablabd, nhcparticipante, database1):
    nhclista1 = [database1.nhcparticipante for database1 in database1.query.all()]
    nhclistasuma = nhclista1
    
    nhclistalimpio = list(filter((nhcparticipante).__ne__, nhclistasuma))
    return nhclistalimpio


# mostrar el pdf en una nueva ventana del navegador
def mostrar_pdf(filepath):

    with open(filepath,"rb") as f:
        pdf_b64 = base64.b64encode(f.read()).decode("utf-8")

    src= f"data:application/pdf;base64,{pdf_b64}"
    js_code = f"""
    var iframe = "<iframe width='100%' height='100%' src='{src}'></iframe>"
    var w = window.open();
    w.document.open();
    w.document.write(iframe);
    w.document.close();
    w.document.title = '{filepath}';
    """
    display(Javascript(js_code))


# fin funciones ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////















# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# pagina de inicio /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# inicio (en esta pagina hay que definir los botones grandes que crean cada tipo de participante)

@appcarasrealistas.route("/", methods=["GET", "POST"])
def inicio():
    if request.method =='POST':

        if request.form.get('botoncrearinicio') == "Crear Nuevo Participante":
            return redirect(url_for('mostrarformularioregistro', tipoparticipante="control"))
        
        # este se eliminará al final y se sustituye por el nav
        if request.form.get('botonsalirinicio') == "Cerrar Programa":
            return redirect(url_for('salir'))

    # este tipolayout es el de inicio, el del nav grande
    tipolayout = 'layoutinicio.html'
    return render_template("inicio.html", tipolayout=tipolayout)


# fin pagina de inicio /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////








# pagina lista de participantes ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# esta es la pagina de la lista de participantes registrados en la aplicacion mediante el formulario de registro

@appcarasrealistas.route("/listaparticipantes/<string:tipoparticipante>/", methods=["GET", "POST"])
def listaparticipantes(tipoparticipante=""):

    if tipoparticipante == "control":
        nombretablabd = Formularioregistro
        tipolayout = 'layoutinicio2.html'
    
    # Para obtener todos los participantes de registrados y mandarlos al html para generar la lista
    listaparticipantes = nombretablabd.query.all()
    numeroparticipantes = len(listaparticipantes)

    return render_template("listaparticipantes.html", tipolayout=tipolayout, tipoparticipante=tipoparticipante, listaparticipantes=listaparticipantes, numeroparticipantes=numeroparticipantes)



# fin pagina lista de participantes ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////








# pagina lista formularios del participante ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# para generar la lista de formularios secundarios y escalas del participante, es decir, los formularios y escalas que pertenecen a cada participante

@appcarasrealistas.route("/listaformulariosparticipante/<string:tipoparticipante>/<int:idparticipante>/<string:nhcparticipante>/<string:fechacreacion>/", methods=["GET", "POST"])
def listaformulariosparticipante(tipoparticipante="", idparticipante=None, nhcparticipante="", fechacreacion=""):
    if request.method == 'POST':

        if request.form.get('salirparticipante') == "Salir del Participante":
            
            return redirect(url_for('listaparticipantes', tipoparticipante=tipoparticipante))
    

    if tipoparticipante == "control":
        # hay que pasar los datos de todas las formularios secundarios y escalas en su version estable e inestable (21 escalas)

        datosformularioantecedentesestable = buscarfirstparticipante(Formularioantecedentes, idparticipante, nhcparticipante, fechacreacion)
        datosescalapanasestable = buscarfirstparticipante(Escalapanas, idparticipante, nhcparticipante, fechacreacion)
        datoscuestionarioavataresestable = buscarfirstparticipante(Cuestionarioavatares, idparticipante, nhcparticipante, fechacreacion)
        datosappcaraspantallaestable = buscarfirstparticipanteappcaras(Appcaraspantalla, idparticipante, nhcparticipante)
        

        tipolayout = 'layoutinicio2.html'
        return render_template("listaformulariosparticipante.html", tipolayout=tipolayout, tipoparticipante=tipoparticipante, idparticipante=idparticipante, nhcparticipante=nhcparticipante, fechacreacion=fechacreacion, 
                                datosformularioantecedentesestable = datosformularioantecedentesestable, datosescalapanasestable = datosescalapanasestable,
                                datoscuestionarioavataresestable = datoscuestionarioavataresestable, datosappcaraspantallaestable = datosappcaraspantallaestable)

# fin pagina lista formularios del participante ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////









# pagina formulario de registro del participante ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# para crear y modificar el formulario de registro, y para crear el esquema de los formularios secundarios y escalas 

@appcarasrealistas.route("/formularioregistro/<string:tipoparticipante>/", methods=["GET", "POST"])
@appcarasrealistas.route("/formularioregistro/<string:tipoparticipante>/<int:idparticipante>/", methods=["GET", "POST"])
def mostrarformularioregistro(tipoparticipante="", idparticipante=None ):
    if request.method == 'POST':

        if tipoparticipante == "control":
            nombretablabd = Formularioregistro
            listaescalas = [Formularioantecedentes, Escalapanas, Cuestionarioavatares]
            listaappcaras = [Appcaraspantalla]

        if request.form.get('botonformularioregistrocrear') == "Crear Participante":
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # definir donde se guardan los datos que provienen del html en las columas del formulario de registro (cada formulario de registro tiene las suyas)
            nhcparticipante = request.form.get('nhcparticipante')
            edad = request.form.get('edad')
            genero = request.form.get('genero')
            if request.form.get('genero') == "Otro:":
                textogenero = request.form.get('textogenero1')
            else:
                textogenero = request.form.get('textogenero2')
            etnia = request.form.get('etnia')
            estadocivil = request.form.get('estadocivil')
            provinciaresidencia = request.form.get('provinciaresidencia')
            if request.form.get('provinciaresidencia') == "Otro:":
                textoprovinciaresidencia = request.form.get('textoprovinciaresidencia1')
            else:
                textoprovinciaresidencia = request.form.get('textoprovinciaresidencia2')
            residencia = request.form.get('residencia')
            estudios = request.form.get('estudios')
            situacionprofesional = request.form.get('situacionprofesional')
            if request.form.get('situacionprofesional') == "Otro:":
                textosituacionprofesional = request.form.get('textosituacionprofesional1')
            else:
                textosituacionprofesional = request.form.get('textosituacionprofesional2')
            profesion = request.form.get('profesion')

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # para definir la fecha de creacion del participante
            fechacreacion = datetime.datetime.today().strftime('%d-%m-%Y %H:%M:%S')

            formulariogeneral = nombretablabd(nhcparticipante=nhcparticipante, fechacreacion=fechacreacion, edad=edad, genero=genero, textogenero=textogenero, etnia=etnia, estadocivil=estadocivil, provinciaresidencia=provinciaresidencia, textoprovinciaresidencia=textoprovinciaresidencia, residencia=residencia, estudios=estudios, situacionprofesional=situacionprofesional, textosituacionprofesional=textosituacionprofesional, profesion=profesion)

            # validacion nhc unico  y que sea distinto a "" y que sea un numero entero
            nhccomprobacion = request.form.get('nhcparticipante')

            nhclista = nhclistatotal(Formularioregistro)

            if (nhccomprobacion in nhclista) or (nhccomprobacion == "") or (not nhccomprobacion.isdigit()):
                formularioregistro = formulariogeneral
                if (nhccomprobacion in nhclista):
                    flash ("El NHC introducido ya se encuentra en la base de datos, por favor introduce un NHC válido", category="borrar")
                elif (nhccomprobacion == ""):
                    flash ("Introduce el NHC del participante", category="borrar")
                elif (not nhccomprobacion.isdigit()):
                    flash ("El NHC debe ser un número entero", category="borrar")
                
                tipolayout = 'layoutinicio2.html'
                return render_template("formularioregistro.html", tipolayout=tipolayout, tipoparticipante=tipoparticipante, idparticipante=idparticipante, formularioregistro=formularioregistro)
            
            else:
                db.session.add(formulariogeneral)
                db.session.commit()
                
                # obtener el idparticipante del participante creado
                idparticipante = formulariogeneral.idparticipante

                # obtener el nhcparticipante del participante creado
                nhcparticipante = formulariogeneral.nhcparticipante
                
                # colocar los todos formularios secundarios y escalas a crear por primera vez
                for escala in listaescalas:
                    crearparticipanteescala(escala, idparticipante, nhcparticipante, fechacreacion)

                flash (f"Se ha creado el participante con NHC: {nhcparticipante} correctamente", category="crear")
                # al pulsar crear nos lleva al las escalas del participantes teniendo en cuenta el tipo de participante (hay que modificar la ruta segun el tipo de participante)
                return redirect(url_for('listaformulariosparticipante', tipoparticipante=tipoparticipante,  idparticipante = idparticipante, nhcparticipante = nhcparticipante, fechacreacion = fechacreacion))


        if request.form.get('botonformularioregistroguardar') == "Guardar Cambios":
            formularioget = getparticipanteporid(nombretablabd, idparticipante)
            # para obtener el nhc antiguo para realizar la busqueda en las escalas
            nhcantiguo = formularioget.nhcparticipante

            # funcion para obtener lista de todos los nhc del programa sin el nhc del participante
            nhclista = nhclistasinid(nombretablabd, nhcantiguo, Formularioregistro)
            #nhclista = nhclistasinid(nombretablabd, idparticipante, Formularioregistro)

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los elementos delos formularios a modificar a partir del elemento de la tabla
            formularioget.nhcparticipante = request.form.get('nhcparticipante')
            formularioget.edad = request.form.get('edad')
            formularioget.genero = request.form.get('genero')
            if request.form.get('genero') == "Otro:":
                formularioget.textogenero = request.form.get('textogenero1')
            else:
                formularioget.textogenero = request.form.get('textogenero2')
            formularioget.etnia = request.form.get('etnia')
            formularioget.estadocivil = request.form.get('estadocivil')
            formularioget.provinciaresidencia = request.form.get('provinciaresidencia')
            if request.form.get('provinciaresidencia') == "Otro:":
                formularioget.textoprovinciaresidencia = request.form.get('textoprovinciaresidencia1')
            else:
                formularioget.textoprovinciaresidencia = request.form.get('textoprovinciaresidencia2')
            formularioget.residencia = request.form.get('residencia')
            formularioget.estudios = request.form.get('estudios')
            formularioget.situacionprofesional = request.form.get('situacionprofesional')
            if request.form.get('situacionprofesional') == "Otro:":
                formularioget.textosituacionprofesional = request.form.get('textosituacionprofesional1')
            else:
                formularioget.textosituacionprofesional = request.form.get('textosituacionprofesional2')
            formularioget.profesion = request.form.get('profesion')

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # para definir la fecha de ultima modificacion del participante
            formularioget.fechaultimamodificacion = datetime.datetime.today().strftime('%d-%m-%Y %H:%M:%S')

            # validacion nhc unico  y que sea distinto a "" y que sea un numero entero
            nhccomprobacion = request.form.get('nhcparticipante')


            # funcion para obtener lista de todos los nhc del programa sin el nhc del participante

            if (nhccomprobacion in nhclista) or (nhccomprobacion == "") or (not nhccomprobacion.isdigit()):
                formularioregistro = formularioget
                if (nhccomprobacion in nhclista):
                    flash ("El NHC introducido ya se encuentra en la base de datos, por favor introduce un NHC válido", category="borrar")
                elif (nhccomprobacion == ""):
                    flash ("Introduce el NHC del participante", category="borrar")
                elif (not nhccomprobacion.isdigit()):
                    flash ("El NHC debe ser un número entero", category="borrar")
                
                tipolayout = 'layoutinicio2.html'
                return render_template("formularioregistro.html", tipolayout=tipolayout, tipoparticipante=tipoparticipante, idparticipante=idparticipante, formularioregistro=formularioregistro)
            
            else:

                db.session.add(formularioget)
                db.session.commit()

                # para obtener el nhc nuevo para introducirlo en las escalas
                nhcnuevo = request.form.get('nhcparticipante')

                # para obtener la fecha de creacion para buscar el participante en las escalas a modificar
                fechacreacion = formularioget.fechacreacion

                # colocar los formularios y escalas para modificar el idparticipante asociado y el nhc, buscarlos aplicando filtros, seleccionando la tabla mediante un bucle
                for escala in listaescalas:
                    modificarnhc(escala, idparticipante, nhcantiguo, nhcnuevo, fechacreacion)
                for appcaras in listaappcaras:
                    modificarnhccaras(appcaras, idparticipante, nhcantiguo, nhcnuevo)


                flash ("Se ha modificado el Formulario de Registro del participante correctamente", category="modificar")
                # al pulsar guardar nos lleva al listado de participantes del tipo del participante (hay que modificar la ruta segun el tipo de participante)
                return redirect(url_for('listaparticipantes', tipoparticipante=tipoparticipante))
        

        if request.form.get('botonformularioregistrovolver') == "Volver Sin Guardar":
            # al pulsar volver nos lleva al listado de participantes del tipo del participante (hay que modificar la ruta segun el tipo de participante)
            return redirect(url_for('listaparticipantes', tipoparticipante=tipoparticipante))


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    if tipoparticipante == "control":
        nombretablabd = Formularioregistro
        tipolayout = 'layoutinicio2.html'


    if idparticipante:
        # si existe idparticipante lo que hace es coger el participante de formulario de registro para ese idparticipante, para pasar los datos al html y que los muestre
        formularioregistro = getparticipanteporid(nombretablabd, idparticipante)

    else:
        # colocar la funcion inicio de cada formmulario para que se muestren bien los placeholders en los html
        formularioregistro = inicioformularioregistro(nombretablabd)

    return render_template("formularioregistro.html", tipolayout=tipolayout, tipoparticipante=tipoparticipante, idparticipante=idparticipante, formularioregistro=formularioregistro)


# fin pagina formulario de registro del participante ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////






















# formularios secundarios y escalas del participante ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# formulario antecedentes ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



@appcarasrealistas.route("/formularioantecedentes/<string:tipoparticipante>/<string:estadoparticipante>/<int:idparticipante>/<string:nhcparticipante>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarformularioantecedentes(tipoparticipante="", estadoparticipante="", idparticipante=None, nhcparticipante="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            #  hay que ver que la escala pertenezca a al tipo de participante, sino no es necesaria colocar la condicion
            if tipoparticipante == "control":
                if estadoparticipante =="estable":
                    nombretablabd = Formularioantecedentes
            

            formularioget = buscarfirstparticipante(nombretablabd, idparticipante, nhcparticipante, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala

            formularioget.antecedentespersonalessomaticos = request.form.get('antecedentespersonalessomaticos')
            
            formularioget.diagnosticodms5 = request.form.get('diagnosticodms5')
            formularioget.faseenfermedadactual = request.form.get('faseenfermedadactual')
            formularioget.edadiniciosintomatologia = request.form.get('edadiniciosintomatologia')
            formularioget.anosevolucionenfermedad = request.form.get('anosevolucionenfermedad')
            formularioget.numerodescompensaciones = request.form.get('numerodescompensaciones')
            formularioget.numerodescompensaciones6meses = request.form.get('numerodescompensaciones6meses')
            formularioget.numeroingresos = request.form.get('numeroingresos')
            formularioget.numeroingresos6meses = request.form.get('numeroingresos6meses')
            formularioget.tratamientopsicofarmacologico = request.form.get('tratamientopsicofarmacologico')
            formularioget.tratamientomedicoactual = request.form.get('tratamientomedicoactual')

            if request.form.get('antecedentespersonalestoxicos1') =="Tabaco.":
                formularioget.antecedentespersonalestoxicos1 = request.form.get('antecedentespersonalestoxicos1')
            else:
                formularioget.antecedentespersonalestoxicos1 = request.form.get('textoantecedentespersonalestoxicos2')

            if request.form.get('antecedentespersonalestoxicos2') =="Alcohol.":
                formularioget.antecedentespersonalestoxicos2 = request.form.get('antecedentespersonalestoxicos2')
            else:
                formularioget.antecedentespersonalestoxicos2 = request.form.get('textoantecedentespersonalestoxicosdepresion2')

            if request.form.get('antecedentespersonalestoxicos8') =="Cafeína.":
                formularioget.antecedentespersonalestoxicos8 = request.form.get('antecedentespersonalestoxicos8')
            else:
                formularioget.antecedentespersonalestoxicos8 = request.form.get('textoantecedentespersonalestoxicos2')

            if request.form.get('antecedentespersonalestoxicos3') =="Cocaína.":
                formularioget.antecedentespersonalestoxicos3 = request.form.get('antecedentespersonalestoxicos3')
            else:
                formularioget.antecedentespersonalestoxicos3 = request.form.get('textoantecedentespersonalestoxicos2')

            if request.form.get('antecedentespersonalestoxicos4') =="Opiáceos.":
                formularioget.antecedentespersonalestoxicos4 = request.form.get('antecedentespersonalestoxicos4')
            else:
                formularioget.antecedentespersonalestoxicos4 = request.form.get('textoantecedentespersonalestoxicos2')

            if request.form.get('antecedentespersonalestoxicos5') =="Cannabis.":
                formularioget.antecedentespersonalestoxicos5 = request.form.get('antecedentespersonalestoxicos5')
            else:
                formularioget.antecedentespersonalestoxicos5 = request.form.get('textoantecedentespersonalestoxicos2')

            if request.form.get('antecedentespersonalestoxicos6') =="Anfetaminas.":
                formularioget.antecedentespersonalestoxicos6 = request.form.get('antecedentespersonalestoxicos6')
            else:
                formularioget.antecedentespersonalestoxicos6 = request.form.get('textoantecedentespersonalestoxicos2')

            if request.form.get('antecedentespersonalestoxicos7') =="Otro:":
                formularioget.antecedentespersonalestoxicos7 = request.form.get('antecedentespersonalestoxicos7')
            else:
                formularioget.antecedentespersonalestoxicos7 = request.form.get('textoantecedentespersonalestoxicos2')

            if request.form.get('antecedentespersonalestoxicos7') == "Otro:":
                formularioget.textoantecedentespersonalestoxicos = request.form.get('textoantecedentespersonalestoxicos')
            else:
                formularioget.textoantecedentespersonalestoxicos = request.form.get('textoantecedentespersonalestoxicos2')

            formularioget.criteriosabuso = request.form.get('criteriosabuso')
            formularioget.antecedentesfamiliarespsiquiatricos = request.form.get('antecedentesfamiliarespsiquiatricos')


            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            formularioget.fechaultimamodificacion = datetime.datetime.today().strftime('%d-%m-%Y %H:%M:%S')
            formularioget.estadoescala = "En Proceso o Finalizada"

            db.session.add(formularioget)
            db.session.commit()
            
            if (request.form.get('botonescalaguardar') == "Guardar"):
                flash ("Se ha guardado el formulario correctamente", category="crear")

            elif (request.form.get('botonescalaguardar') == "Guardar Cambios"):
                flash ("Se ha modificado el formulario correctamente", category="modificar")
            
            return redirect(url_for('listaformulariosparticipante', tipoparticipante=tipoparticipante, idparticipante = idparticipante, nhcparticipante = nhcparticipante, fechacreacion=fechacreacion))


        if request.form.get('botonescalavolver') == "Volver Sin Guardar":
            return redirect(url_for('listaformulariosparticipante', tipoparticipante=tipoparticipante, idparticipante = idparticipante, nhcparticipante = nhcparticipante, fechacreacion=fechacreacion))


    #  hay que ver que la escala pertenezca a al tipo de participante, sino no es necesaria colocar la condicion
    if tipoparticipante == "control":
        if estadoparticipante =="estable":
            nombretablabd = Formularioantecedentes
        tipolayout = 'layoutescalascontrol.html'
    

    formulariosecundario = buscarfirstparticipante(nombretablabd, idparticipante, nhcparticipante, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearparticipanteescala(nombretablabd, idparticipante, nhcparticipante, fechacreacion)

    return render_template("formularioantecedentes.html", tipolayout=tipolayout, tipoparticipante=tipoparticipante, idparticipante=idparticipante, nhcparticipante=nhcparticipante, formulariosecundario=formulariosecundario)











# escala panas ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasrealistas.route("/escalapanas/<string:tipoparticipante>/<string:estadoparticipante>/<int:idparticipante>/<string:nhcparticipante>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalapanas(tipoparticipante="", estadoparticipante="", idparticipante=None, nhcparticipante="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            if tipoparticipante == "control":
                if estadoparticipante =="estable":
                    nombretablabd = Escalapanas

            formularioget = buscarfirstparticipante(nombretablabd, idparticipante, nhcparticipante, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala
            formularioget.escalapanas1 = request.form.get('escalapanas1')
            formularioget.escalapanas2 = request.form.get('escalapanas2')
            formularioget.escalapanas3 = request.form.get('escalapanas3')
            formularioget.escalapanas4 = request.form.get('escalapanas4')
            formularioget.escalapanas5 = request.form.get('escalapanas5')
            formularioget.escalapanas6 = request.form.get('escalapanas6')
            formularioget.escalapanas7 = request.form.get('escalapanas7')
            formularioget.escalapanas8 = request.form.get('escalapanas8')
            formularioget.escalapanas9 = request.form.get('escalapanas9')
            formularioget.escalapanas10 = request.form.get('escalapanas10')
            formularioget.escalapanas11 = request.form.get('escalapanas11')
            formularioget.escalapanas12 = request.form.get('escalapanas12')
            formularioget.escalapanas13 = request.form.get('escalapanas13')
            formularioget.escalapanas14 = request.form.get('escalapanas14')
            formularioget.escalapanas15 = request.form.get('escalapanas15')
            formularioget.escalapanas16 = request.form.get('escalapanas16')
            formularioget.escalapanas17 = request.form.get('escalapanas17')
            formularioget.escalapanas18 = request.form.get('escalapanas18')
            formularioget.escalapanas19 = request.form.get('escalapanas19')
            formularioget.escalapanas20 = request.form.get('escalapanas20')

            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            formularioget.fechaultimamodificacion = datetime.datetime.today().strftime('%d-%m-%Y %H:%M:%S')
            formularioget.estadoescala = "En Proceso o Finalizada"

            db.session.add(formularioget)
            db.session.commit()
            
            if (request.form.get('botonescalaguardar') == "Guardar"):
                flash ("Se ha guardado la escala correctamente", category="crear")
                
            elif (request.form.get('botonescalaguardar') == "Guardar Cambios"):
                flash ("Se ha modificado la escala correctamente", category="modificar")
            
            return redirect(url_for('listaformulariosparticipante', tipoparticipante=tipoparticipante, idparticipante = idparticipante, nhcparticipante = nhcparticipante, fechacreacion=fechacreacion))


        if request.form.get('botonescalavolver') == "Volver Sin Guardar":
            return redirect(url_for('listaformulariosparticipante', tipoparticipante=tipoparticipante, idparticipante = idparticipante, nhcparticipante = nhcparticipante, fechacreacion=fechacreacion))


    #  hay que ver que la escala pertenezca a al tipo de participante, sino no es necesaria colocar la condicion

    if tipoparticipante == "control":
        if estadoparticipante =="estable":
            nombretablabd = Escalapanas
        tipolayout = 'layoutescalascontrol.html'

    formulariosecundario = buscarfirstparticipante(nombretablabd, idparticipante, nhcparticipante, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearparticipanteescala(nombretablabd, idparticipante, nhcparticipante, fechacreacion)

    return render_template("/escalapanas.html", tipolayout=tipolayout, tipoparticipante=tipoparticipante, idparticipante=idparticipante, nhcparticipante=nhcparticipante, formulariosecundario=formulariosecundario)


















# cuestionario avatares ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@appcarasrealistas.route("/cuestionarioavatares/<string:tipoparticipante>/<string:estadoparticipante>/<int:idparticipante>/<string:nhcparticipante>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarcuestionarioavatares(tipoparticipante="", estadoparticipante="", idparticipante=None, nhcparticipante="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            if tipoparticipante == "control":
                if estadoparticipante =="estable":
                    nombretablabd = Cuestionarioavatares


            formularioget = buscarfirstparticipante(nombretablabd, idparticipante, nhcparticipante, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala
            formularioget.cuestionarioavatares1 = request.form.get('cuestionarioavatares1')
            formularioget.cuestionarioavatares2 = request.form.get('cuestionarioavatares2')
            formularioget.cuestionarioavatares3 = request.form.get('cuestionarioavatares3')
            formularioget.cuestionarioavatares4 = request.form.get('cuestionarioavatares4')
            formularioget.cuestionarioavatares5_1 = request.form.get('cuestionarioavatares5_1')
            formularioget.cuestionarioavatares5_2 = request.form.get('cuestionarioavatares5_2')
            formularioget.cuestionarioavatares5_3 = request.form.get('cuestionarioavatares5_3')
            formularioget.cuestionarioavatares6 = request.form.get('cuestionarioavatares6')
            formularioget.cuestionarioavatares7 = request.form.get('cuestionarioavatares7')
            formularioget.cuestionarioavatares8 = request.form.get('cuestionarioavatares8')
            formularioget.cuestionarioavatares9 = request.form.get('cuestionarioavatares9')

            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            formularioget.fechaultimamodificacion = datetime.datetime.today().strftime('%d-%m-%Y %H:%M:%S')
            formularioget.estadoescala = "En Proceso o Finalizada"

            db.session.add(formularioget)
            db.session.commit()
            
            if (request.form.get('botonescalaguardar') == "Guardar"):
                flash ("Se ha guardado la escala correctamente", category="crear")
                
            elif (request.form.get('botonescalaguardar') == "Guardar Cambios"):
                flash ("Se ha modificado la escala correctamente", category="modificar")
            
            return redirect(url_for('listaformulariosparticipante', tipoparticipante=tipoparticipante, idparticipante = idparticipante, nhcparticipante = nhcparticipante, fechacreacion=fechacreacion))


        if request.form.get('botonescalavolver') == "Volver Sin Guardar":
            return redirect(url_for('listaformulariosparticipante', tipoparticipante=tipoparticipante, idparticipante = idparticipante, nhcparticipante = nhcparticipante, fechacreacion=fechacreacion))


    #  hay que ver que la escala pertenezca a al tipo de participante, sino no es necesaria colocar la condicion

    if tipoparticipante == "control":
        if estadoparticipante =="estable":
            nombretablabd = Cuestionarioavatares
        tipolayout = 'layoutescalascontrol.html'


    formulariosecundario = buscarfirstparticipante(nombretablabd, idparticipante, nhcparticipante, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearparticipanteescala(nombretablabd, idparticipante, nhcparticipante, fechacreacion)

    return render_template("/cuestionarioavatares.html", tipolayout=tipolayout, tipoparticipante=tipoparticipante, idparticipante=idparticipante, nhcparticipante=nhcparticipante, formulariosecundario=formulariosecundario)


# fin formularios secundarios y escalas del participante ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




































#  Appcaraspantalla del participante ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@appcarasrealistas.route('/appcaraspantalla/<string:tipoparticipante>/<string:estadoparticipante>/<int:idparticipante>/<string:nhcparticipante>/<string:fechacreacion>/', methods=['GET','POST'])
def appcaraspantalla(tipoparticipante="", estadoparticipante="", idparticipante=None, nhcparticipante="", fechacreacion=""):

    if tipoparticipante == "control":
        rutabasedatos = "dbappcarasrealistas.db"
        
        if estadoparticipante == "estable":
            tipoparticipanteapp = "Participante_control_Estable"
            nombretabla = "appcaraspantalla"


    # Abre la aplicacion de las caras y le envia la informacion necesaria a los participantes
    Popen("start carasPantalla.exe "+ str(nhcparticipante) + " " + str(idparticipante) + " " + str(tipoparticipanteapp) + " " + str(rutabasedatos) + " " + str(nombretabla) , shell= True)

    return render_template('layoutappcaras.html', tipoapp='pantalla', estadoparticipante=estadoparticipante, tipoparticipante=tipoparticipante, idparticipante=idparticipante, nhcparticipante=nhcparticipante, fechacreacion=fechacreacion)


#  fin Appcaraspantalla del participante ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




#  Resultados Appcaraspantalla del participante ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@appcarasrealistas.route('/resultadosparticipanteappcaraspantalla/<string:tipoparticipante>/<string:estadoparticipante>/<int:idparticipante>/<string:nhcparticipante>/<string:fechacreacion>/', methods=['GET','POST'])
def resultadosparticipanteappcaraspantalla(tipoparticipante="", estadoparticipante="", idparticipante=None, nhcparticipante="", fechacreacion=""):
    if request.method == 'POST':

        if request.form.get('resultadosvolver') == "Volver al Participante":
            return redirect(url_for('listaformulariosparticipante', tipoparticipante=tipoparticipante, idparticipante = idparticipante, nhcparticipante = nhcparticipante, fechacreacion=fechacreacion))


    if tipoparticipante == "control":
        tipolayout = "layoutresultadoscontrol.html"
        
        if estadoparticipante == "estable":
            nombretablabd = Appcaraspantalla

    # buscar aciertos por emocion
    emociones = ['0', '1', '2', '3', '4', '5', '6']
    porcentajes = []
    datosappcaras = []

    for emocion in emociones:
        aciertos = buscarallaciertosparticipanteappcaras(nombretablabd, idparticipante, nhcparticipante, emocion)
        countaciertos = len(aciertos)
        porcentaje = (countaciertos * 100) / 8
        porcentajes.append(porcentaje)

    datosappcaras = buscarallparticipanteappcaras(nombretablabd, idparticipante, nhcparticipante)

    return render_template('layoutresultadosappcaras.html', porcentajes=porcentajes , datosappcaras=datosappcaras, tipolayout=tipolayout,  tipoparticipante=tipoparticipante, estadoparticipante=estadoparticipante, idparticipante=idparticipante, nhcparticipante=nhcparticipante, fechacreacion=fechacreacion)


#  fin Resultados Appcaraspantalla del participante ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




#  Descargar Resultados Appcaraspantalla del participante ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@appcarasrealistas.route('/descargarresultadosparticipanteappcaraspantalla/<string:tipoparticipante>/<string:estadoparticipante>/<int:idparticipante>/<string:nhcparticipante>/<string:fechacreacion>/', methods=['GET','POST'])
def descargarresultadosparticipanteappcaraspantalla(tipoparticipante="", estadoparticipante="", idparticipante=None, nhcparticipante="", fechacreacion=""):

    if tipoparticipante == "control":
        tipolayout = "layoutresultadoscontrol.html"
        
        if estadoparticipante == "estable":
            nombretablabd = Appcaraspantalla


    # busqueda del codigo de la aplicacion
    if estadoparticipante == "estable":
        codigoaplicacion = "-RFN-E"

    codigo = nhcparticipante + codigoaplicacion



    # buscar aciertos por emocion y definir datos del gráfico creado con plotly y kaleido
    emociones = ['Neutral', 'Sorpresa', 'Miedo', 'Ira', 'Asco', 'Alegría', 'Tristeza']
    porcentajes = []
    label_ys = ['0.0', '12.5', '25.0', '37.5', '50.0', '62.5', '75.0', '87.5', '100.0']
    label_y = [0.0, 12.5, 25.0, 37.5, 50.0, 62.5, 75.0, 87.5, 100.0]
    label = []

    for i in range(7):
        aciertos = buscarallaciertosparticipanteappcaras(nombretablabd, idparticipante, nhcparticipante, str(i))
        countaciertos = len(aciertos)
        porcentaje = (countaciertos * 100) / 8
        porcentajes.append(porcentaje)
        label.append(str(porcentaje) + '%')




    # datos de fecha y hora a la que se crea el pdf
    fecha = datetime.datetime.today().strftime('%d-%m-%Y')
    hora = datetime.datetime.today().strftime('%H-%M-%S')
    horatext = hora.replace('-', ':')



    #datos del gráfico creado con plotly import plotly.express as px
    fig2 = px.bar(
        x=emociones,
        y=porcentajes,
        text = label,
        color=["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#cd3e95", "#cd763e"], 
        color_discrete_map="identity",
        title="Porcentaje de aciertos por cada tipo de emoción mostrada:",

        labels=dict(x="Emociones", y="Porcentaje de Aciertos (%)")
        )
    
    fig2.update_traces(textposition='outside')
    fig2.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='rgba(0,0,0,0)')


    fig2.update_yaxes(
        tick0=0.0, 
        dtick=12.5,
        range = [0.0, 110.0])

    fig2.update_layout(
        title_x=0.5,

        yaxis = dict(
            tickmode = 'array',
            tickvals = label_y,
            ticktext = label_ys
            )
        )

    fig2.update_xaxes(ticks="inside", title_standoff = 10)
    fig2.update_yaxes(ticks="inside", col=1, title_standoff = 10)

    fig2.update_xaxes(showline=True, linewidth=2, linecolor='black')
    fig2.update_yaxes(showline=True, linewidth=2, linecolor='black')

    #fig2.update_yaxes(showgrid=True, gridwidth=2, gridcolor='Gray')

    fig2.to_image(format="png", width=600, height=350, scale=1)
    fig2.write_image(f"static/pdf/{ codigo }.png")



    # # creacion del pdf con fpdf2

    # definicion de la disposicion, unidades y tamaño del la pagina
    pdf = PDF('P', 'mm', 'A4')
        
    # alias para seber el numero de pagina
    pdf.alias_nb_pages()

    # añadir una pagina
    pdf.add_page()

    # definir margenes del pdf
    pdf.set_margins(20, 25, 20)

    pdf.set_y(50)

    # establecer el tipo de letra
    pdf.set_font('helvetica','', 12)
    
    # añadir el texto de la pagina
    pdf.multi_cell(170, 10, f"En el programa de 'Reconocimiento Facial de Emociones en Realidad Virtual No Inmersiva', el participante con código: { codigo }, ha conseguido los porcentajes de aciertos para cada una de las emociones indicadas a continuación:", 0, 'J', 0)

    pdf.ln(10)
    # añadir la imagen del grafico a la pagina
    pdf.image(f"static/pdf/{ codigo }.png", x=25, y=90, w = 170)


    # se define la posicion de la linea
    pdf.set_y(-40)
    # se define la fuente del footer
    pdf.set_font('helvetica', 'I', 8)
    # Color de texto en gris
    pdf.set_text_color(128)
    # se define el texto del footer
    pdf.cell(0, 10, f'Este documento .pdf ha sido generado el { fecha } a las { horatext }.', align='L')

    # para cerrar y salir del pdf
    pdf.output(f"static/pdf/{ codigo }.pdf")


    # definir la ruta del escritorio o en descargas
    #rutadesktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    rutadescargas = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')

    # copiar el documento en la ruta con el nombre del codigo, fecha y hora de generacion del pdf
    #shutil.copy(f'static/pdf/{ codigo }.pdf', os.path.join(rutadesktop, codigo + '_Fecha_'+ fecha + '_Hora_'+ hora +'.pdf'))
    shutil.copy(f'static/pdf/{ codigo }.pdf', os.path.join(rutadescargas, codigo + '_Fecha_'+ fecha + '_Hora_'+ hora +'.pdf'))

    #eliminar la imagen y el pdf de la carpeta image para que no se sature con archivos innecesarios
    os.remove(f'static/pdf/{ codigo }.png')
    os.remove(f'static/pdf/{ codigo }.pdf')

    flash(f"Se ha guardado el archivo '{ codigo }_Fecha_{ fecha }_Hora_{ hora }.pdf' en la carpeta 'Descargas' con los resultados de la 'Aplicación de Reconocimiento Facial en Realidad Virtual No Inmersiva', para el participante con NHC: { nhcparticipante } en estado { estadoparticipante }.", category="crear")

    return redirect(url_for('listaformulariosparticipante', tipoparticipante=tipoparticipante, idparticipante = idparticipante, nhcparticipante = nhcparticipante, fechacreacion=fechacreacion))


#  fin descargar Resultados Appcaraspantalla del participante ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////










# reinicio app caraspantalla ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Para reinicio un participante por completo

@appcarasrealistas.route('/borrardatosparticipanteappcaraspantalla/<string:tipoparticipante>/<string:estadoparticipante>/<int:idparticipante>/<string:nhcparticipante>/<string:fechacreacion>/', methods=["GET", "POST"])
def borrardatosparticipanteappcaraspantalla(tipoparticipante="", estadoparticipante="", idparticipante=None, nhcparticipante="", fechacreacion=""):
    # colocar los formulario y escalas que se desean eliminar
        
    if tipoparticipante == "control":
        if estadoparticipante == "estable":
            listaappcaras = [Appcaraspantalla]

    # borra los todos los datos del participante de la aplicacion caras (sacar las escalas de las listas anteriores)
    for appcara in listaappcaras:
        borrarappcaras(appcara, idparticipante, nhcparticipante)

    flash ("Se han borrado los datos y reiniciado la Aplicación Caras No Inmersiva correctamente", category="borrar")
    return redirect(url_for('listaformulariosparticipante', tipoparticipante=tipoparticipante, idparticipante = idparticipante, nhcparticipante = nhcparticipante, fechacreacion=fechacreacion))


# fin reinicio appcaraspantalla ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////























# borrado completo del participante ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Para borrar un participante por completo

@appcarasrealistas.route('/borrarparticipante/<string:tipoparticipante>/<int:idparticipante>/<string:nhcparticipante>/<string:fechacreacion>/', methods=["GET", "POST"])
def borrarparticipante(tipoparticipante="", idparticipante=None, nhcparticipante="", fechacreacion=""):
    # colocar los formulario y escalas que se desean eliminar
        

    if tipoparticipante == "control":
        listaescalas = [Formularioregistro, Formularioantecedentes,Escalapanas, Cuestionarioavatares]
        listaappcaras = [Appcaraspantalla]

    # borra los todos los datos del participante en los formularios secundarios y escalas
    for escala in listaescalas:
        borrarescala(escala, idparticipante, nhcparticipante, fechacreacion)

    # borra los todos los datos del participante de la aplicacion caras (sacar las escalas de las listas anteriores)
    for appcara in listaappcaras:
        borrarappcaras(appcara, idparticipante, nhcparticipante)



    flash ("Se ha eliminado el participante correctamente", category="borrar")
    return redirect(url_for('listaparticipantes', tipoparticipante=tipoparticipante))


# fin borrado completo del participante ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# Boton exportar base datos ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@appcarasrealistas.route('/exportarbase')
def exportarbase():

    # colocar la ruta donde se crea el directorio
    # parent_dir = 'c:/'
    parent_dir = 'C:\\'
    directory1 = 'Registro-Datos_App'
    path1 = os.path.join(parent_dir, directory1)

    fechaexportacion = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    direcciondestino = os.path.join(path1, 'Bases-de-Datos-' + fechaexportacion)


    # copiar bases de datos
    if not os.path.exists(direcciondestino):
        os.makedirs(direcciondestino)

    shutil.copy('database/dbappcarasrealistas.db', direcciondestino)
    
    flash (f"Se han exportado las bases de datos correctamente en el directorio {path1} con fecha: {fechaexportacion} ", category="exportar")
    
    return redirect(url_for('inicio'))


# fin Boton exportar base datos ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# Boton cerrar programa ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Para cerrar el programa y el navegador:

@appcarasrealistas.route('/salir')
def salir():

    Popen('taskkill /F /IM brave.exe', shell=True)
    time.sleep(2)

    Popen('taskkill /F /IM carasPantalla.exe', shell=True)

    time.sleep(5)

    pid = os.getpid()
    os.kill(pid, signal.SIGINT)

    return


# fin Boton cerrar programa ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


if __name__ == '__main__':

    # para cerrar si hay alguna de las aplicaciones abiertas antes de iniciar la aplicación
    Popen('taskkill /F /IM brave.exe', shell=True)
    time.sleep(2)
    
    Popen('taskkill /F /IM carasPantalla.exe', shell=True)

    time.sleep(1)

    # crea la base de datos si no se encuentra
    db.create_all()

    # genera un puerto 5004 (metodo en el que se utiliza Popen)
    Popen("start brave -incognito -start-maximized /new_tab 127.0.0.1:5004", shell= True)

    time.sleep(1)

    appcarasrealistas.run(port=5004, debug=False)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


