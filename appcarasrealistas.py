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
appcarasrealistas.config['SQLALCHEMY_BINDS'] = {'datosbipolar': 'sqlite:///database/dbcarasdatosbipolar.db'}
appcarasrealistas.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(appcarasrealistas)

# crear las tablas y las columnas de la base de datos
# para añadir el modelo a la base de datos desde terminal:
# python
# from appcarasrealistas import db
# db.create_all(bind=['datosbipolar'])
# exit()



# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Tabla datos formulario para paciente bipolar

class Formularioregistrobipolar(db.Model):
    __bind_key__ = 'datosbipolar'
    # identificador del paciente
    idpaciente = db.Column(db.Integer, primary_key=True)

    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    # numero historial clinico del paciente
    nhcpaciente = db.Column(db.Text)
    
    # datos sociodemograficos del paciente
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
    


# Tabla datos formulario secundario para paciente con bipolar (cantidad 2)

class Formularioantecedentesbipolarestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)
    
    # datos antecedentes personales somáticos para paciente con bipolar
    antecedentespersonalessomaticos = db.Column(db.Text)
    
    # datos antecedentes personales psiquiatricos para paciente bipolar
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

# Tabla datos paciente bipolar en estado estable

class Escalapanasbipolarestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
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


class Appcaraspantallabipolarestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idnumericoappcaras = db.Column(db.Integer, primary_key=True)

    # datos fijos en cada fila appcaras
    idnumericopaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

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
    
    

class Appcarasvrbipolarestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idnumericoappcaras = db.Column(db.Integer, primary_key=True)

    # datos fijos en cada fila appcaras
    idnumericopaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

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
    r_eye = db.Column(db.Text)
    l_eye = db.Column(db.Text)
    nose = db.Column(db.Text)
    front = db.Column(db.Text)
    mouth = db.Column(db.Text)
    r_cheek = db.Column(db.Text)
    l_cheek = db.Column(db.Text)
    top_left = db.Column(db.Text)
    top_right = db.Column(db.Text)
    bottom_left = db.Column(db.Text)
    bottom_right = db.Column(db.Text)
    distancia = db.Column(db.Text)


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Cuestionarioavataresbipolarestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
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





# funciones ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# funciones para iniciar los formularios con los valores por defecto, para que se muestren bien los placeholders del html
def inicioformularioregistro(nombretablabd):
    formulario = nombretablabd(nhcpaciente ="", edad ="", textogenero ="", textoprovinciaresidencia ="", textosituacionprofesional ="", profesion ="")
    return formulario


# funcion get en sqlalchemy
def getpacienteporid(nombretablabd, idpaciente):
    datopaciente = nombretablabd.query.get(idpaciente)
    return datopaciente


# funcion para crear el paciente en cada escala
def crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion):

    # escalas depresion estable

    if (nombretablabd == Formularioantecedentesdepresionestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="depresion", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", antecedentespersonalessomaticos="", diagnosticodms5="", edadiniciosintomatologia="", anosevolucionenfermedad="", numerodescompensaciones="", numeroingresos="", numerodescompensaciones6meses="", tratamientopsicofarmacologico="", tratamientomedicoactual="", antecedentesfamiliarespsiquiatricos="", textoantecedentespersonalestoxicos="", numeroingresos6meses="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalaminicertsdepresionestable) or (nombretablabd == Escalaius12depresionestable) or (nombretablabd == Escalaebrddepresionestable) or (nombretablabd == Escalabdiiidepresionestable) or (nombretablabd == Escalashortstairdepresionestable) or (nombretablabd == Escalahrsddepresionestable) or (nombretablabd == Escalapanasdepresionestable) or (nombretablabd == Escalafastdepresionestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="depresion", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalawhoqoldepresionestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="depresion", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalawhoqol27="", escalawhoqol28="", escalawhoqol29="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalaeeagdepresionestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="depresion", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalaeeag1="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala
    
    if (nombretablabd == Cuestionarioavataresdepresionestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="depresion", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", cuestionarioavatares9="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    # escalas depresion inestable

    if (nombretablabd == Formularioantecedentesdepresioninestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="depresion", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", antecedentespersonalessomaticos="", diagnosticodms5="", edadiniciosintomatologia="", anosevolucionenfermedad="", numerodescompensaciones="", numeroingresos="", numerodescompensaciones6meses="", tratamientopsicofarmacologico="", tratamientomedicoactual="", antecedentesfamiliarespsiquiatricos="", textoantecedentespersonalestoxicos="", numeroingresos6meses="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalaminicertsdepresioninestable) or (nombretablabd == Escalaius12depresioninestable) or (nombretablabd == Escalaebrddepresioninestable) or (nombretablabd == Escalabdiiidepresioninestable) or (nombretablabd == Escalashortstairdepresioninestable) or (nombretablabd == Escalahrsddepresioninestable) or (nombretablabd == Escalapanasdepresioninestable) or (nombretablabd == Escalafastdepresioninestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="depresion", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalawhoqoldepresioninestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="depresion", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalawhoqol27="", escalawhoqol28="", escalawhoqol29="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalaeeagdepresioninestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="depresion", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalaeeag1="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Cuestionarioavataresdepresioninestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="depresion", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", cuestionarioavatares9="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    # ///////////////////////////////////////////////////////////////////////////////////////

    # escalas bipolar estable

    if (nombretablabd == Formularioantecedentesbipolarestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="bipolar", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", antecedentespersonalessomaticos="", diagnosticodms5="", edadiniciosintomatologia="", anosevolucionenfermedad="", numerodescompensaciones="", numeroingresos="", numerodescompensaciones6meses="", tratamientopsicofarmacologico="", tratamientomedicoactual="", antecedentesfamiliarespsiquiatricos="", textoantecedentespersonalestoxicos="", numeroingresos6meses="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalamadrsbipolarestable) or (nombretablabd == Escalaymrsbipolarestable) or (nombretablabd == Escalapanasbipolarestable) or (nombretablabd == Escalafastbipolarestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="bipolar", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala
    
    if (nombretablabd == Escalawhoqolbipolarestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="bipolar", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalawhoqol27="", escalawhoqol28="", escalawhoqol29="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalaeeagbipolarestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="bipolar", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalaeeag1="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Cuestionarioavataresbipolarestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="bipolar", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", cuestionarioavatares9="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    # escalas bipolar inestable

    if (nombretablabd == Formularioantecedentesbipolarinestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="bipolar", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", antecedentespersonalessomaticos="", diagnosticodms5="", edadiniciosintomatologia="", anosevolucionenfermedad="", numerodescompensaciones="", numeroingresos="", numerodescompensaciones6meses="", tratamientopsicofarmacologico="", tratamientomedicoactual="", antecedentesfamiliarespsiquiatricos="", textoantecedentespersonalestoxicos="", numeroingresos6meses="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalamadrsbipolarinestable) or (nombretablabd == Escalaymrsbipolarinestable) or (nombretablabd == Escalapanasbipolarinestable) or (nombretablabd == Escalafastbipolarinestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="bipolar", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalawhoqolbipolarinestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="bipolar", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalawhoqol27="", escalawhoqol28="", escalawhoqol29="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalaeeagbipolarinestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="bipolar", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalaeeag1="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Cuestionarioavataresbipolarinestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="bipolar", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", cuestionarioavatares9="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala



    # ///////////////////////////////////////////////////////////////////////////////////////

    # escalas esquizofrenia estable

    if (nombretablabd == Formularioantecedentesesquizofreniaestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizofrenia", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", antecedentespersonalessomaticos="", diagnosticodms5="", edadiniciosintomatologia="", anosevolucionenfermedad="", numerodescompensaciones="", numeroingresos="", numerodescompensaciones6meses="", tratamientopsicofarmacologico="", tratamientomedicoactual="", antecedentesfamiliarespsiquiatricos="", textoantecedentespersonalestoxicos="", numeroingresos6meses="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalapanssesquizofreniaestable) or (nombretablabd == Escalapanasesquizofreniaestable) or (nombretablabd == Escalafastesquizofreniaestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizofrenia", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalawhoqolesquizofreniaestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizofrenia", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalawhoqol27="", escalawhoqol28="", escalawhoqol29="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalaeeagesquizofreniaestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizofrenia", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalaeeag1="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Cuestionarioavataresesquizofreniaestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizofrenia", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", cuestionarioavatares9="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    # escalas esquizofrenia inestable

    if (nombretablabd == Formularioantecedentesesquizofreniainestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizofrenia", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", antecedentespersonalessomaticos="", diagnosticodms5="", edadiniciosintomatologia="", anosevolucionenfermedad="", numerodescompensaciones="", numeroingresos="", numerodescompensaciones6meses="", tratamientopsicofarmacologico="", tratamientomedicoactual="", antecedentesfamiliarespsiquiatricos="", textoantecedentespersonalestoxicos="", numeroingresos6meses="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalapanssesquizofreniainestable) or (nombretablabd == Escalapanasesquizofreniainestable) or (nombretablabd == Escalafastesquizofreniainestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizofrenia", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalawhoqolesquizofreniainestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizofrenia", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalawhoqol27="", escalawhoqol28="", escalawhoqol29="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalaeeagesquizofreniainestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizofrenia", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalaeeag1="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Cuestionarioavataresesquizofreniainestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizofrenia", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", cuestionarioavatares9="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    # ///////////////////////////////////////////////////////////////////////////////////////

    # escalas esquizoafectivo estable

    if (nombretablabd == Formularioantecedentesesquizoafectivoestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizoafectivo", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", antecedentespersonalessomaticos="", diagnosticodms5="", edadiniciosintomatologia="", anosevolucionenfermedad="", numerodescompensaciones="", numeroingresos="", numerodescompensaciones6meses="", tratamientopsicofarmacologico="", tratamientomedicoactual="", antecedentesfamiliarespsiquiatricos="", textoantecedentespersonalestoxicos="", numeroingresos6meses="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalapanssesquizoafectivoestable) or (nombretablabd == Escalamadrsesquizoafectivoestable) or (nombretablabd == Escalaymrsesquizoafectivoestable) or (nombretablabd == Escalapanasesquizoafectivoestable) or (nombretablabd == Escalafastesquizoafectivoestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizoafectivo", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalawhoqolesquizoafectivoestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizoafectivo", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalawhoqol27="", escalawhoqol28="", escalawhoqol29="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalaeeagesquizoafectivoestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizoafectivo", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalaeeag1="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Cuestionarioavataresesquizoafectivoestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizoafectivo", estadopaciente="estable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", cuestionarioavatares9="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    # escalas esquizoafectivo inestable

    if (nombretablabd == Formularioantecedentesesquizoafectivoinestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizoafectivo", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", antecedentespersonalessomaticos="", diagnosticodms5="", edadiniciosintomatologia="", anosevolucionenfermedad="", numerodescompensaciones="", numeroingresos="", numerodescompensaciones6meses="", tratamientopsicofarmacologico="", tratamientomedicoactual="", antecedentesfamiliarespsiquiatricos="", textoantecedentespersonalestoxicos="", numeroingresos6meses="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalapanssesquizoafectivoinestable) or (nombretablabd == Escalamadrsesquizoafectivoinestable) or (nombretablabd == Escalaymrsesquizoafectivoinestable) or (nombretablabd == Escalapanasesquizoafectivoinestable) or (nombretablabd == Escalafastesquizoafectivoinestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizoafectivo", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalawhoqolesquizoafectivoinestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizoafectivo", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalawhoqol27="", escalawhoqol28="", escalawhoqol29="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Escalaeeagesquizoafectivoinestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizoafectivo", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", escalaeeag1="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    if (nombretablabd == Cuestionarioavataresesquizoafectivoinestable):
        escala = nombretablabd(idpaciente = idpaciente, nhcpaciente = nhcpaciente, tipopaciente="esquizoafectivo", estadopaciente="inestable", estadoescala="Sin rellenar", fechacreacion=fechacreacion, fechaultimamodificacion="", cuestionarioavatares9="")
        db.session.add(escala)
        db.session.commit()
        inicio = escala

    return inicio


# funcion para modificar los nhc de los formularios secundarios y de las escalas
def modificarnhc(nombretablabd, idpaciente, nhcantiguo, nhcnuevo, fechacreacion):
    formulario = nombretablabd.query.filter_by(fechacreacion = fechacreacion).filter_by(idpaciente = idpaciente).filter_by(nhcpaciente = nhcantiguo).all()
    for n in formulario:
        n.nhcpaciente = nhcnuevo
        db.session.add(n)
        db.session.commit()

# funcion para modificar los nhc de los formularios appcaras
def modificarnhccaras(nombretablabd, idpaciente, nhcantiguo, nhcnuevo):
    formulario = nombretablabd.query.filter_by(idnumericopaciente = idpaciente).filter_by(nhcpaciente = nhcantiguo).all()
    for n in formulario:
        n.nhcpaciente = nhcnuevo
        db.session.add(n)
        db.session.commit()






# funcion para buscar el primer registro el paciente en cada escala
def buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion):
    buscarfirst = nombretablabd.query.filter_by(fechacreacion = fechacreacion).filter_by(idpaciente = idpaciente).filter_by(nhcpaciente = nhcpaciente).first()
    return buscarfirst

def buscarfirstpacienteappcaras(nombretablabd, idpaciente, nhcpaciente):
    buscarfirst = nombretablabd.query.filter_by(idnumericopaciente = idpaciente).filter_by(nhcpaciente = nhcpaciente).first()
    return buscarfirst

def buscarallpacienteappcaras(nombretablabd, idpaciente, nhcpaciente):
    buscarall = nombretablabd.query.filter_by(idnumericopaciente = idpaciente).filter_by(nhcpaciente = nhcpaciente).all()
    return buscarall

def buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, emocion):
    #buscarallaciertos = nombretablabd.query.filter_by(idnumericopaciente = idpaciente).filter_by(nhcpaciente = nhcpaciente).filter_by(respuestacorrecta = emocion).filter_by(acierto = "1").all()
    buscarallaciertos = nombretablabd.query.filter_by(idnumericopaciente = idpaciente).filter_by(nhcpaciente = nhcpaciente).filter_by(respuestacorrectafiltrada = emocion).filter_by(acierto = "1").all()
    return buscarallaciertos





# funcion para borrar el paciente en los formularios secundarios y en las escalas
def borrarescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion):
    formulario = nombretablabd.query.filter_by(fechacreacion = fechacreacion).filter_by(nhcpaciente = nhcpaciente).filter_by(idpaciente = idpaciente).all()
    for n in formulario:
        db.session.delete(n)
        db.session.commit()

def borrarappcaras(nombretablabd, idpaciente, nhcpaciente):
    borrarappcaras = nombretablabd.query.filter_by(nhcpaciente=nhcpaciente).filter_by(idnumericopaciente=idpaciente).all()
    for n in borrarappcaras:
        db.session.delete(n)
        db.session.commit()



# funcion para obtener lista de todos los nhc del programa
def nhclistatotal(database1, database2, database3, database4):
    nhclista1 = [database1.nhcpaciente for database1 in database1.query.all()]
    nhclista2 = [database2.nhcpaciente for database2 in database2.query.all()]
    nhclista3 = [database3.nhcpaciente for database3 in database3.query.all()]
    nhclista4 = [database3.nhcpaciente for database3 in database3.query.all()]
    nhclistasuma = nhclista1 + nhclista2 + nhclista3 + nhclista4
    return nhclistasuma


# # funcion para obtener lista de todos los nhc del programa sin el nhc del paciente
# def nhclistasinid(nombretablabd, idpaciente, database1, database2, database3, database4):
#     nhclista1 = [database1.nhcpaciente for database1 in database1.query.all()]
#     nhclista2 = [database2.nhcpaciente for database2 in database2.query.all()]
#     nhclista3 = [database3.nhcpaciente for database3 in database3.query.all()]
#     nhclista4 = [database3.nhcpaciente for database3 in database3.query.all()]
#     nhclistasuma = nhclista1 + nhclista2 + nhclista3 + nhclista4
    
#     datospaciente = nombretablabd.query.get(idpaciente)
    
#     nhceliminar = datospaciente.nhcpaciente
#     nhclistalimpio = list(filter((nhceliminar).__ne__, nhclistasuma))
    
#     return nhclistalimpio


# funcion para obtener lista de todos los nhc del programa sin el nhc del paciente
def nhclistasinid(nombretablabd, nhcpaciente, database1, database2, database3, database4):
    nhclista1 = [database1.nhcpaciente for database1 in database1.query.all()]
    nhclista2 = [database2.nhcpaciente for database2 in database2.query.all()]
    nhclista3 = [database3.nhcpaciente for database3 in database3.query.all()]
    nhclista4 = [database3.nhcpaciente for database3 in database3.query.all()]
    nhclistasuma = nhclista1 + nhclista2 + nhclista3 + nhclista4
    
    nhclistalimpio = list(filter((nhcpaciente).__ne__, nhclistasuma))
    return nhclistalimpio








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







# pagina de inicio /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# inicio (en esta pagina hay que definir los botones grandes que crean cada tipo de paciente)

@appcarasrealistas.route("/", methods=["GET", "POST"])
def inicio():
    if request.method =='POST':
        if request.form.get('botoncrearinicio') == "Crear Paciente con Trastorno Depresivo Mayor":
            return redirect(url_for('mostrarformularioregistro', tipopaciente="depresion"))

        elif request.form.get('botoncrearinicio') == "Crear Paciente con Trastorno Bipolar":
            return redirect(url_for('mostrarformularioregistro', tipopaciente="bipolar"))

        elif request.form.get('botoncrearinicio') == "Crear Paciente con Trastorno del Espectro de la Esquizofrenia":
            return redirect(url_for('mostrarformularioregistro', tipopaciente="esquizofrenia"))

        elif request.form.get('botoncrearinicio') == "Crear Paciente con Trastorno Esquizoafectivo":
            return redirect(url_for('mostrarformularioregistro', tipopaciente="esquizoafectivo"))
        
        # este se eliminará al final y se sustituye por el nav
        if request.form.get('botonsalirinicio') == "Cerrar Programa":
            return redirect(url_for('salir'))

    # este tipolayout es el de inicio, el del nav grande
    tipolayout = 'layoutinicio.html'
    return render_template("inicio.html", tipolayout=tipolayout)


# fin pagina de inicio /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////








# pagina lista de pacientes ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# esta es la pagina de la lista de pacientes registrados en la aplicacion mediante el formulario de registro

@appcarasrealistas.route("/listapacientes/<string:tipopaciente>/", methods=["GET", "POST"])
def listapacientes(tipopaciente=""):

    if tipopaciente == "bipolar":
        nombretablabd = Formularioregistrobipolar
        tipolayout = 'layoutinicio2.html'
    
    # Para obtener todos los pacientes de registrados y mandarlos al html para generar la lista
    listapacientes = nombretablabd.query.all()
    numeropacientes = len(listapacientes)

    return render_template("listapacientes.html", tipolayout=tipolayout, tipopaciente=tipopaciente, listapacientes=listapacientes, numeropacientes=numeropacientes)



# fin pagina lista de pacientes ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////








# pagina lista formularios del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# para generar la lista de formularios secundarios y escalas del paciente, es decir, los formularios y escalas que pertenecen a cada paciente

@appcarasrealistas.route("/listaformulariospaciente/<string:tipopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def listaformulariospaciente(tipopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':

        if request.form.get('salirpaciente') == "Salir del Paciente":
            
            return redirect(url_for('listapacientes', tipopaciente=tipopaciente))
    

    if tipopaciente == "bipolar":
        # hay que pasar los datos de todas las formularios secundarios y escalas en su version estable e inestable (21 escalas)

        datosformularioantecedentesestable = buscarfirstpaciente(Formularioantecedentesbipolarestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalapanasestable = buscarfirstpaciente(Escalapanasbipolarestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalafastestable = buscarfirstpaciente(Escalafastbipolarestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalawhoqolestable = buscarfirstpaciente(Escalawhoqolbipolarestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalaeeagestable = buscarfirstpaciente(Escalaeeagbipolarestable, idpaciente, nhcpaciente, fechacreacion)
        datoscuestionarioavataresestable = buscarfirstpaciente(Cuestionarioavataresbipolarestable, idpaciente, nhcpaciente, fechacreacion)
        
        datosappcaraspantallaestable = buscarfirstpacienteappcaras(Appcaraspantallabipolarestable, idpaciente, nhcpaciente)
        datosappcarasvrestable = buscarfirstpacienteappcaras(Appcarasvrbipolarestable, idpaciente, nhcpaciente)

        datosescalamadrsestable = buscarfirstpaciente(Escalamadrsbipolarestable, idpaciente, nhcpaciente, fechacreacion) 
        datosescalaymrsestable = buscarfirstpaciente(Escalaymrsbipolarestable, idpaciente, nhcpaciente, fechacreacion)


        datosformularioantecedentesinestable = buscarfirstpaciente(Formularioantecedentesbipolarinestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalapanasinestable = buscarfirstpaciente(Escalapanasbipolarinestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalafastinestable = buscarfirstpaciente(Escalafastbipolarinestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalawhoqolinestable = buscarfirstpaciente(Escalawhoqolbipolarinestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalaeeaginestable = buscarfirstpaciente(Escalaeeagbipolarinestable, idpaciente, nhcpaciente, fechacreacion)
        datoscuestionarioavataresinestable = buscarfirstpaciente(Cuestionarioavataresbipolarinestable, idpaciente, nhcpaciente, fechacreacion)
        
        datosappcaraspantallainestable = buscarfirstpacienteappcaras(Appcaraspantallabipolarinestable, idpaciente, nhcpaciente)
        datosappcarasvrinestable = buscarfirstpacienteappcaras(Appcarasvrbipolarinestable, idpaciente, nhcpaciente)

        datosescalamadrsinestable = buscarfirstpaciente(Escalamadrsbipolarinestable, idpaciente, nhcpaciente, fechacreacion) 
        datosescalaymrsinestable = buscarfirstpaciente(Escalaymrsbipolarinestable, idpaciente, nhcpaciente, fechacreacion)

        tipolayout = 'layoutinicio2.html'
        return render_template("listaformulariospaciente.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, fechacreacion=fechacreacion, datosformularioantecedentesestable = datosformularioantecedentesestable, datosescalapanasestable = datosescalapanasestable, datosescalafastestable = datosescalafastestable, datosescalawhoqolestable = datosescalawhoqolestable, datosescalaeeagestable = datosescalaeeagestable, datoscuestionarioavataresestable = datoscuestionarioavataresestable, datosappcaraspantallaestable = datosappcaraspantallaestable, datosappcarasvrestable = datosappcarasvrestable, datosescalamadrsestable = datosescalamadrsestable, datosescalaymrsestable = datosescalaymrsestable, datosformularioantecedentesinestable = datosformularioantecedentesinestable, datosescalapanasinestable = datosescalapanasinestable, datosescalafastinestable = datosescalafastinestable, datosescalawhoqolinestable = datosescalawhoqolinestable, datosescalaeeaginestable = datosescalaeeaginestable, datoscuestionarioavataresinestable = datoscuestionarioavataresinestable, datosappcaraspantallainestable = datosappcaraspantallainestable, datosappcarasvrinestable = datosappcarasvrinestable, datosescalamadrsinestable = datosescalamadrsinestable, datosescalaymrsinestable = datosescalaymrsinestable)



# fin pagina lista formularios del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////









# pagina formulario de registro del paciente ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# para crear y modificar el formulario de registro, y para crear el esquema de los formularios secundarios y escalas 

@appcarasrealistas.route("/formularioregistro/<string:tipopaciente>/", methods=["GET", "POST"])
@appcarasrealistas.route("/formularioregistro/<string:tipopaciente>/<int:idpaciente>/", methods=["GET", "POST"])
def mostrarformularioregistro(tipopaciente="", idpaciente=None ):
    if request.method == 'POST':

        if tipopaciente == "bipolar":
            nombretablabd = Formularioregistrobipolar
            listaescalas = [Formularioantecedentesbipolarestable, Formularioantecedentesbipolarinestable, Escalamadrsbipolarestable, Escalaymrsbipolarestable, Escalapanasbipolarestable, Escalafastbipolarestable, Escalawhoqolbipolarestable, Escalaeeagbipolarestable, Cuestionarioavataresbipolarestable, Escalamadrsbipolarinestable, Escalaymrsbipolarinestable, Escalapanasbipolarinestable, Escalafastbipolarinestable, Escalawhoqolbipolarinestable, Escalaeeagbipolarinestable, Cuestionarioavataresbipolarinestable]
            listaappcaras = [Appcaraspantallabipolarestable, Appcarasvrbipolarestable, Appcaraspantallabipolarinestable, Appcarasvrbipolarinestable]

        if request.form.get('botonformularioregistrocrear') == "Crear Paciente":
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # definir donde se guardan los datos que provienen del html en las columas del formulario de registro (cada formulario de registro tiene las suyas)
            nhcpaciente = request.form.get('nhcpaciente')
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
            # para definir la fecha de creacion del paciente
            fechacreacion = datetime.datetime.today().strftime('%d-%m-%Y %H:%M:%S')

            formulariogeneral = nombretablabd(nhcpaciente=nhcpaciente, fechacreacion=fechacreacion, edad=edad, genero=genero, textogenero=textogenero, etnia=etnia, estadocivil=estadocivil, provinciaresidencia=provinciaresidencia, textoprovinciaresidencia=textoprovinciaresidencia, residencia=residencia, estudios=estudios, situacionprofesional=situacionprofesional, textosituacionprofesional=textosituacionprofesional, profesion=profesion)

            # validacion nhc unico  y que sea distinto a "" y que sea un numero entero
            nhccomprobacion = request.form.get('nhcpaciente')

            nhclista = nhclistatotal(Formularioregistrodepresion, Formularioregistrobipolar, Formularioregistroesquizofrenia, Formularioregistroesquizoafectivo)

            if (nhccomprobacion in nhclista) or (nhccomprobacion == "") or (not nhccomprobacion.isdigit()):
                formularioregistro = formulariogeneral
                if (nhccomprobacion in nhclista):
                    flash ("El NHC introducido ya se encuentra en la base de datos, por favor introduce un NHC válido", category="borrar")
                elif (nhccomprobacion == ""):
                    flash ("Introduce el NHC del paciente", category="borrar")
                elif (not nhccomprobacion.isdigit()):
                    flash ("El NHC debe ser un número entero", category="borrar")
                
                tipolayout = 'layoutinicio2.html'
                return render_template("formularioregistro.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, formularioregistro=formularioregistro)
            
            else:
                db.session.add(formulariogeneral)
                db.session.commit()
                
                # obtener el idpaciente del paciente creado
                idpaciente = formulariogeneral.idpaciente

                # obtener el nhcpaciente del paciente creado
                nhcpaciente = formulariogeneral.nhcpaciente
                
                # colocar los todos formularios secundarios y escalas a crear por primera vez
                for escala in listaescalas:
                    crearpacienteescala(escala, idpaciente, nhcpaciente, fechacreacion)

                flash (f"Se ha creado el paciente con NHC: {nhcpaciente} correctamente", category="crear")
                # al pulsar crear nos lleva al las escalas del pacientes teniendo en cuenta el tipo de paciente (hay que modificar la ruta segun el tipo de paciente)
                return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente,  idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion = fechacreacion))


        if request.form.get('botonformularioregistroguardar') == "Guardar Cambios":
            formularioget = getpacienteporid(nombretablabd, idpaciente)
            # para obtener el nhc antiguo para realizar la busqueda en las escalas
            nhcantiguo = formularioget.nhcpaciente

            # funcion para obtener lista de todos los nhc del programa sin el nhc del paciente
            nhclista = nhclistasinid(nombretablabd, nhcantiguo, Formularioregistrodepresion, Formularioregistrobipolar, Formularioregistroesquizofrenia, Formularioregistroesquizoafectivo)
            #nhclista = nhclistasinid(nombretablabd, idpaciente, Formularioregistrodepresion, Formularioregistrobipolar, Formularioregistroesquizofrenia, Formularioregistroesquizoafectivo)

            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los elementos delos formularios a modificar a partir del elemento de la tabla
            formularioget.nhcpaciente = request.form.get('nhcpaciente')
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
            # para definir la fecha de ultima modificacion del paciente
            formularioget.fechaultimamodificacion = datetime.datetime.today().strftime('%d-%m-%Y %H:%M:%S')

            # validacion nhc unico  y que sea distinto a "" y que sea un numero entero
            nhccomprobacion = request.form.get('nhcpaciente')


            # funcion para obtener lista de todos los nhc del programa sin el nhc del paciente

            if (nhccomprobacion in nhclista) or (nhccomprobacion == "") or (not nhccomprobacion.isdigit()):
                formularioregistro = formularioget
                if (nhccomprobacion in nhclista):
                    flash ("El NHC introducido ya se encuentra en la base de datos, por favor introduce un NHC válido", category="borrar")
                elif (nhccomprobacion == ""):
                    flash ("Introduce el NHC del paciente", category="borrar")
                elif (not nhccomprobacion.isdigit()):
                    flash ("El NHC debe ser un número entero", category="borrar")
                
                tipolayout = 'layoutinicio2.html'
                return render_template("formularioregistro.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, formularioregistro=formularioregistro)
            
            else:

                db.session.add(formularioget)
                db.session.commit()

                # para obtener el nhc nuevo para introducirlo en las escalas
                nhcnuevo = request.form.get('nhcpaciente')

                # para obtener la fecha de creacion para buscar el paciente en las escalas a modificar
                fechacreacion = formularioget.fechacreacion

                # colocar los formularios y escalas para modificar el idpaciente asociado y el nhc, buscarlos aplicando filtros, seleccionando la tabla mediante un bucle
                for escala in listaescalas:
                    modificarnhc(escala, idpaciente, nhcantiguo, nhcnuevo, fechacreacion)
                for appcaras in listaappcaras:
                    modificarnhccaras(appcaras, idpaciente, nhcantiguo, nhcnuevo)


                flash ("Se ha modificado el Formulario de Registro del paciente correctamente", category="modificar")
                # al pulsar guardar nos lleva al listado de pacientes del tipo del paciente (hay que modificar la ruta segun el tipo de paciente)
                return redirect(url_for('listapacientes', tipopaciente=tipopaciente))
        

        if request.form.get('botonformularioregistrovolver') == "Volver Sin Guardar":
            # al pulsar volver nos lleva al listado de pacientes del tipo del paciente (hay que modificar la ruta segun el tipo de paciente)
            return redirect(url_for('listapacientes', tipopaciente=tipopaciente))


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    if tipopaciente == "bipolar":
        nombretablabd = Formularioregistrobipolar
        tipolayout = 'layoutinicio2.html'


    if idpaciente:
        # si existe idpaciente lo que hace es coger el paciente de formulario de registro para ese idpaciente, para pasar los datos al html y que los muestre
        formularioregistro = getpacienteporid(nombretablabd, idpaciente)

    else:
        # colocar la funcion inicio de cada formmulario para que se muestren bien los placeholders en los html
        formularioregistro = inicioformularioregistro(nombretablabd)

    return render_template("formularioregistro.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, formularioregistro=formularioregistro)


# fin pagina formulario de registro del paciente ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////






















# formularios secundarios y escalas del paciente ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# formulario antecedentes ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



@appcarasrealistas.route("/formularioantecedentes/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarformularioantecedentes(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            #  hay que ver que la escala pertenezca a al tipo de paciente, sino no es necesaria colocar la condicion
            if tipopaciente == "bipolar":
                if estadopaciente =="estable":
                    nombretablabd = Formularioantecedentesbipolarestable
                elif estadopaciente =="inestable":
                    nombretablabd = Formularioantecedentesbipolarinestable
            

            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
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
            
            return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))


        if request.form.get('botonescalavolver') == "Volver Sin Guardar":
            return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))


    #  hay que ver que la escala pertenezca a al tipo de paciente, sino no es necesaria colocar la condicion
    if tipopaciente == "bipolar":
        if estadopaciente =="estable":
            nombretablabd = Formularioantecedentesbipolarestable
        elif estadopaciente =="inestable":
            nombretablabd = Formularioantecedentesbipolarinestable
        tipolayout = 'layoutescalasdepresion.html'
    

    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("formularioantecedentes.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)











# escala panas ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasrealistas.route("/escalapanas/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalapanas(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            if tipopaciente == "bipolar":
                if estadopaciente =="estable":
                    nombretablabd = Escalapanasbipolarestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalapanasbipolarinestable

            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
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
            
            return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))


        if request.form.get('botonescalavolver') == "Volver Sin Guardar":
            return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))


    #  hay que ver que la escala pertenezca a al tipo de paciente, sino no es necesaria colocar la condicion

    if tipopaciente == "bipolar":
        if estadopaciente =="estable":
            nombretablabd = Escalapanasbipolarestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalapanasbipolarinestable
        tipolayout = 'layoutescalasbipolar.html'

    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/escalapanas.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)















# cuestionario avatares ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasrealistas.route("/cuestionarioavatares/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarcuestionarioavatares(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            if tipopaciente == "bipolar":
                if estadopaciente =="estable":
                    nombretablabd = Cuestionarioavataresbipolarestable
                elif estadopaciente =="inestable":
                    nombretablabd = Cuestionarioavataresbipolarinestable

            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
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
            
            return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))


        if request.form.get('botonescalavolver') == "Volver Sin Guardar":
            return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))


    #  hay que ver que la escala pertenezca a al tipo de paciente, sino no es necesaria colocar la condicion

    if tipopaciente == "bipolar":
        if estadopaciente =="estable":
            nombretablabd = Cuestionarioavataresbipolarestable
        elif estadopaciente =="inestable":
            nombretablabd = Cuestionarioavataresbipolarinestable
        tipolayout = 'layoutescalasbipolar.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/cuestionarioavatares.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)




# fin formularios secundarios y escalas del paciente ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////











#  Appcaraspantalla del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasrealistas.route('/appcaraspantalla/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=['GET','POST'])
def appcaraspantalla(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):

    if tipopaciente == "bipolar":
        rutabasedatos = "dbcarasdatosbipolar.db"
        
        if estadopaciente == "estable":
            tipopacienteapp = "Paciente_Bipolar_Estable"
            nombretabla = "appcaraspantallabipolarestable"
        elif estadopaciente == "inestable":
            tipopacienteapp = "Paciente_Bipolar_Inestable"
            nombretabla = "appcaraspantallabipolarinestable"

    # Abre la aplicacion de las caras y le envia la informacion necesaria a los pacientes
    Popen("start carasPantalla.exe "+ str(nhcpaciente) + " " + str(idpaciente) + " " + str(tipopacienteapp) + " " + str(rutabasedatos) + " " + str(nombretabla) , shell= True)

    return render_template('layoutappcaras.html', tipoapp='pantalla', estadopaciente=estadopaciente, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, fechacreacion=fechacreacion)


#  fin Appcaraspantalla del paciente ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////






#  Resultados Appcaraspantalla del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasrealistas.route('/resultadospacienteappcaraspantalla/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=['GET','POST'])
def resultadospacienteappcaraspantalla(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':

        if request.form.get('resultadosvolver') == "Volver al Paciente":
            return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))


    if tipopaciente == "bipolar":
        tipolayout = "layoutresultadosbipolar.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcaraspantallabipolarestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcaraspantallabipolarinestable


    # buscar aciertos por emocion
    aciertosneutral = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "0")
    countaciertosneutral = len(aciertosneutral)
    porcentajeneutral = (countaciertosneutral * 100 )/ 8

    aciertossorpresa = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "1")
    countaciertossorpresa = len(aciertossorpresa)
    porcentajesorpresa = (countaciertossorpresa * 100 )/ 8

    aciertosmiedo = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "2")
    countaciertosmiedo = len(aciertosmiedo)
    porcentajemiedo = (countaciertosmiedo * 100 )/ 8

    aciertosira = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "3")
    countaciertosira = len(aciertosira)
    porcentajeira = (countaciertosira * 100 )/ 8

    aciertosasco = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "4")
    countaciertosasco = len(aciertosasco)
    porcentajeasco = (countaciertosasco * 100 )/ 8
    
    aciertosalegria = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "5")
    countaciertosalegria = len(aciertosalegria)
    porcentajealegria = (countaciertosalegria * 100 )/ 8

    aciertostristeza = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "6")
    countaciertostristeza = len(aciertostristeza)
    porcentajetristeza = (countaciertostristeza * 100 )/ 8


    porcentajes = [porcentajeneutral, porcentajesorpresa, porcentajemiedo, porcentajeira, porcentajeasco, porcentajealegria, porcentajetristeza]

    datosappcaras = buscarallpacienteappcaras(nombretablabd, idpaciente, nhcpaciente)

    return render_template('layoutresultadosappcaras.html', porcentajes=porcentajes , datosappcaras=datosappcaras, tipolayout=tipolayout,  tipopaciente=tipopaciente, estadopaciente=estadopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, fechacreacion=fechacreacion)


#  fin Resultados Appcaraspantalla del paciente ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////






#  Descargar Resultados Appcaraspantalla del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasrealistas.route('/descargarresultadospacienteappcaraspantalla/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=['GET','POST'])
def descargarresultadospacienteappcaraspantalla(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):

    if tipopaciente == "bipolar":
        tipolayout = "layoutresultadosbipolar.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcaraspantallabipolarestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcaraspantallabipolarinestable



    # buscar aciertos por emocion
    aciertosneutral = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "0")
    countaciertosneutral = len(aciertosneutral)
    porcentajeneutral = (countaciertosneutral * 100 )/ 8

    aciertossorpresa = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "1")
    countaciertossorpresa = len(aciertossorpresa)
    porcentajesorpresa = (countaciertossorpresa * 100 )/ 8

    aciertosmiedo = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "2")
    countaciertosmiedo = len(aciertosmiedo)
    porcentajemiedo = (countaciertosmiedo * 100 )/ 8

    aciertosira = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "3")
    countaciertosira = len(aciertosira)
    porcentajeira = (countaciertosira * 100 )/ 8

    aciertosasco = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "4")
    countaciertosasco = len(aciertosasco)
    porcentajeasco = (countaciertosasco * 100 )/ 8
    
    aciertosalegria = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "5")
    countaciertosalegria = len(aciertosalegria)
    porcentajealegria = (countaciertosalegria * 100 )/ 8

    aciertostristeza = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "6")
    countaciertostristeza = len(aciertostristeza)
    porcentajetristeza = (countaciertostristeza * 100 )/ 8



    # # busqueda del codigo de la aplicacion

    # if len(nhcpaciente) == 1:
    #     nhcmodificado = nhcpaciente
    #     if estadopaciente == "estable":
    #         codigoaplicacion = "RFN-EXXXXX"
    #     elif estadopaciente == "inestable":
    #         codigoaplicacion = "RFN-IXXXXX"
    #     codigocreado = codigoaplicacion + nhcmodificado
    #     codigo = codigocreado
    
    # elif len(nhcpaciente) == 2:
    #     nhcmodificado = nhcpaciente
    #     if estadopaciente == "estable":
    #         codigoaplicacion = "RFN-EXXXX"
    #     elif estadopaciente == "inestable":
    #         codigoaplicacion = "RFN-IXXXX"
    #     codigocreado = codigoaplicacion + nhcmodificado
    #     codigo = codigocreado

    # elif len(nhcpaciente) == 3:
    #     nhcmodificado = nhcpaciente
    #     if estadopaciente == "estable":
    #         codigoaplicacion = "RFN-EXXX"
    #     elif estadopaciente == "inestable":
    #         codigoaplicacion = "RFN-IXXX"
    #     codigocreado = codigoaplicacion + nhcmodificado
    #     codigo = codigocreado

    # elif len(nhcpaciente) == 4:
    #     nhcmodificado = nhcpaciente
    #     if estadopaciente == "estable":
    #         codigoaplicacion = "RFN-EXX"
    #     elif estadopaciente == "inestable":
    #         codigoaplicacion = "RFN-IXX"
    #     codigocreado = codigoaplicacion + nhcmodificado
    #     codigo = codigocreado

    # elif len(nhcpaciente) >= 4:
    #     nhcmodificado = nhcpaciente[-4:]
    #     if estadopaciente == "estable":
    #         codigoaplicacion = "RFN-EXX"
    #     elif estadopaciente == "inestable":
    #         codigoaplicacion = "RFN-IXX"
    #     codigocreado = codigoaplicacion + nhcmodificado
    #     codigo = codigocreado



    # busqueda del codigo de la aplicacion

    if estadopaciente == "estable":
        codigoaplicacion = "-RFN-E"
    elif estadopaciente == "inestable":
        codigoaplicacion = "-RFN-I"
    codigo = nhcpaciente + codigoaplicacion




    # datos de fecha y hora a la que se crea el pdf
    fecha = datetime.datetime.today().strftime('%d-%m-%Y')
    hora = datetime.datetime.today().strftime('%H-%M-%S')
    horatext = hora.replace('-', ':')


    # datos del gráfico creado con plotly y kaleido

    emociones = ['Neutral', 'Sorpresa', 'Miedo', 'Ira', 'Asco', 'Alegría', 'Tristeza']
    porcentajes = [porcentajeneutral, porcentajesorpresa, porcentajemiedo, porcentajeira, porcentajeasco, porcentajealegria, porcentajetristeza]
    label_ys=['0.0', '12.5', '25.0', '37.5', '50.0', '62.5', '75.0', '87.5', '100.0']
    label_y=[0.0, 12.5, 25.0, 37.5, 50.0, 62.5, 75.0, 87.5, 100.0]
    label = [str(porcentajeneutral) + '%', str(porcentajesorpresa) + '%', str(porcentajemiedo) +'%', str(porcentajeira) +'%', str(porcentajeasco) +'%', str(porcentajealegria) +'%', str(porcentajetristeza) +'%']
    

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

    flash(f"Se ha guardado el archivo '{ codigo }_Fecha_{ fecha }_Hora_{ hora }.pdf' en la carpeta 'Descargas' con los resultados de la 'Aplicación de Reconocimiento Facial en Realidad Virtual No Inmersiva', para el paciente con NHC: { nhcpaciente } en estado { estadopaciente }.", category="crear")

    return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))


#  fin descargar Resultados Appcaraspantalla del paciente ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////









# reinicio app caraspantalla ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Para reinicio un paciente por completo

@appcarasrealistas.route('/borrardatospacienteappcaraspantalla/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=["GET", "POST"])
def borrardatospacienteappcaraspantalla(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    # colocar los formulario y escalas que se desean eliminar
        
    if tipopaciente == "bipolar":
        if estadopaciente == "estable":
            listaappcaras = [Appcaraspantallabipolarestable]
        elif estadopaciente == "inestable":
            listaappcaras = [Appcaraspantallabipolarinestable]

    # borra los todos los datos del paciente de la aplicacion caras (sacar las escalas de las listas anteriores)
    for appcara in listaappcaras:
        borrarappcaras(appcara, idpaciente, nhcpaciente)

    flash ("Se han borrado los datos y reiniciado la Aplicación Caras No Inmersiva correctamente", category="borrar")
    return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))


# fin reinicio appcaraspantalla ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////







# borrado completo del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Para borrar un paciente por completo

@appcarasrealistas.route('/borrarpaciente/<string:tipopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=["GET", "POST"])
def borrarpaciente(tipopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    # colocar los formulario y escalas que se desean eliminar
        

    if tipopaciente == "bipolar":
        listaescalas = [Formularioregistrobipolar, Formularioantecedentesbipolarestable, Formularioantecedentesbipolarinestable, Escalamadrsbipolarestable, Escalaymrsbipolarestable, Escalapanasbipolarestable, Escalafastbipolarestable, Escalawhoqolbipolarestable, Escalaeeagbipolarestable, Cuestionarioavataresbipolarestable, Escalamadrsbipolarinestable, Escalaymrsbipolarinestable, Escalapanasbipolarinestable, Escalafastbipolarinestable, Escalawhoqolbipolarinestable, Escalaeeagbipolarinestable, Cuestionarioavataresbipolarinestable]
        listaappcaras = [Appcaraspantallabipolarestable, Appcarasvrbipolarestable, Appcaraspantallabipolarinestable, Appcarasvrbipolarinestable]

    # borra los todos los datos del paciente en los formularios secundarios y escalas
    for escala in listaescalas:
        borrarescala(escala, idpaciente, nhcpaciente, fechacreacion)

    # borra los todos los datos del paciente de la aplicacion caras (sacar las escalas de las listas anteriores)
    for appcara in listaappcaras:
        borrarappcaras(appcara, idpaciente, nhcpaciente)



    flash ("Se ha eliminado el paciente correctamente", category="borrar")
    return redirect(url_for('listapacientes', tipopaciente=tipopaciente))


# fin borrado completo del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////







# Boton exportar base datos ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@appcarasrealistas.route('/exportarbase')
def exportarbase():

    # colocar la ruta donde se crea el directorio
    parent_dir = 'c:/'
    directory1 = 'Registro-Datos-Reconocimiento-Facial'
    path1 = os.path.join(parent_dir, directory1)

    fechaexportacion = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    direcciondestino = os.path.join(path1, 'Bases-de-Datos-' + fechaexportacion)


    # copiar bases de datos
    if not os.path.exists(direcciondestino):
        os.makedirs(direcciondestino)

    shutil.copy('database/dbcarasdatosbipolar.db', direcciondestino)
    
    flash (f"Se han exportado las bases de datos correctamente en el directorio C:\Registro-Datos-Reconocimiento-Facial con fecha: {fechaexportacion} ", category="exportar")
    
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


