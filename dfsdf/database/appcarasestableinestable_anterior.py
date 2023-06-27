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

import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.lib.utils import ImageReader










if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    
    appcarasestableinestable = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

else:
    appcarasestableinestable = Flask(__name__)
    



#creacion de una clave secreta
appcarasestableinestable.secret_key = 'clave_secreta_flask'

# configurar la ruta de las bases de datos
appcarasestableinestable.config['SQLALCHEMY_BINDS'] = {'datosbipolar': 'sqlite:///database/dbcarasdatosbipolar.db', 'datosdepresion': 'sqlite:///database/dbcarasdatosdepresion.db', 'datosesquizofrenia': 'sqlite:///database/dbcarasdatosesquizofrenia.db', 'datosesquizoafectivo': 'sqlite:///database/dbcarasdatosesquizoafectivo.db'}
appcarasestableinestable.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(appcarasestableinestable)

# crear las tablas y las columnas de la base de datos
# para añadir el modelo a la base de datos desde terminal:
# python
# from appcarasestableinestable import db
# db.create_all(bind=['datosbipolar', 'datosdepresion', 'datosesquizofrenia', 'datosesquizoafectivo' ])
# exit()



# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Tabla datos formulario general para paciente con depresion

class Formularioregistrodepresion(db.Model):
    __bind_key__ = 'datosdepresion'
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
    


# Tabla datos formulario secundario para paciente con depresion

class Formularioantecedentesdepresionestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    # datos antecedentes personales somáticos para paciente con depresion
    antecedentespersonalessomaticos = db.Column(db.Text)
    
    # datos antecedentes personales psiquiatricos para paciente con depresion
    diagnosticodms5 = db.Column(db.Text)
    faseenfermedadactual = db.Column(db.Text)
    edadiniciosintomatologia = db.Column(db.Text)
    anosevolucionenfermedad = db.Column(db.Text)
    numerodescompensaciones = db.Column(db.Text)
    numerodescompensaciones6meses = db.Column(db.Text)
    numeroingresos = db.Column(db.Text)
    numeroingresos6meses = db.Column(db.Text)
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

class Formularioantecedentesdepresioninestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    # datos antecedentes personales somáticos para paciente con depresion
    antecedentespersonalessomaticos = db.Column(db.Text)
    
    # datos antecedentes personales psiquiatricos para paciente con depresion
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


# Tabla datos paciente con depresion en estado estable

class Escalaminicertsdepresionestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)

    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaminicerts1 = db.Column(db.Text)
    escalaminicerts2 = db.Column(db.Text)
    escalaminicerts3 = db.Column(db.Text)
    escalaminicerts4 = db.Column(db.Text)
    escalaminicerts5 = db.Column(db.Text)
    escalaminicerts6 = db.Column(db.Text)
    escalaminicerts7 = db.Column(db.Text)
    escalaminicerts8 = db.Column(db.Text)
    escalaminicerts9 = db.Column(db.Text)
    escalaminicerts10 = db.Column(db.Text)
    escalaminicerts11 = db.Column(db.Text)
    escalaminicerts12 = db.Column(db.Text)
    escalaminicerts13 = db.Column(db.Text)
    escalaminicerts14 = db.Column(db.Text)
    escalaminicerts15 = db.Column(db.Text)
    escalaminicerts16 = db.Column(db.Text)


class Escalaius12depresionestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaius12_1 = db.Column(db.Text)
    escalaius12_2 = db.Column(db.Text)
    escalaius12_3 = db.Column(db.Text)
    escalaius12_4 = db.Column(db.Text)
    escalaius12_5 = db.Column(db.Text)
    escalaius12_6 = db.Column(db.Text)
    escalaius12_7 = db.Column(db.Text)
    escalaius12_8 = db.Column(db.Text)
    escalaius12_9 = db.Column(db.Text)
    escalaius12_10 = db.Column(db.Text)
    escalaius12_11 = db.Column(db.Text)
    escalaius12_12 = db.Column(db.Text)



class Escalaebrddepresionestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaebrd1 = db.Column(db.Text)
    escalaebrd2 = db.Column(db.Text)
    escalaebrd3 = db.Column(db.Text)
    escalaebrd4 = db.Column(db.Text)


class Escalabdiiidepresionestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalabdiii1 = db.Column(db.Text)
    escalabdiii2 = db.Column(db.Text)
    escalabdiii3 = db.Column(db.Text)
    escalabdiii4 = db.Column(db.Text)
    escalabdiii5 = db.Column(db.Text)
    escalabdiii6 = db.Column(db.Text)
    escalabdiii7 = db.Column(db.Text)
    escalabdiii8 = db.Column(db.Text)
    escalabdiii9 = db.Column(db.Text)
    escalabdiii10 = db.Column(db.Text)
    escalabdiii11 = db.Column(db.Text)
    escalabdiii12 = db.Column(db.Text)
    escalabdiii13 = db.Column(db.Text)
    escalabdiii14 = db.Column(db.Text)
    escalabdiii15 = db.Column(db.Text)
    escalabdiii16 = db.Column(db.Text)
    escalabdiii17 = db.Column(db.Text)
    escalabdiii18 = db.Column(db.Text)
    escalabdiii19 = db.Column(db.Text)
    escalabdiii20 = db.Column(db.Text)
    escalabdiii21 = db.Column(db.Text)



class Escalashortstairdepresionestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalashortstair1 = db.Column(db.Text)
    escalashortstair2 = db.Column(db.Text)
    escalashortstair3 = db.Column(db.Text)
    escalashortstair4 = db.Column(db.Text)
    escalashortstair5 = db.Column(db.Text)
    escalashortstair6 = db.Column(db.Text)
    escalashortstair7 = db.Column(db.Text)
    escalashortstair8 = db.Column(db.Text)


class Escalahrsddepresionestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalahrsd1 = db.Column(db.Text)
    escalahrsd2 = db.Column(db.Text)
    escalahrsd3 = db.Column(db.Text)
    escalahrsd4 = db.Column(db.Text)
    escalahrsd5 = db.Column(db.Text)
    escalahrsd6 = db.Column(db.Text)
    escalahrsd7 = db.Column(db.Text)
    escalahrsd8 = db.Column(db.Text)
    escalahrsd9 = db.Column(db.Text)
    escalahrsd10 = db.Column(db.Text)
    escalahrsd11 = db.Column(db.Text)
    escalahrsd12 = db.Column(db.Text)
    escalahrsd13 = db.Column(db.Text)
    escalahrsd14 = db.Column(db.Text)
    escalahrsd15 = db.Column(db.Text)
    escalahrsd16 = db.Column(db.Text)
    escalahrsd17 = db.Column(db.Text)



class Escalapanasdepresionestable(db.Model):
    __bind_key__ = 'datosdepresion'
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



class Escalafastdepresionestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalafast1 = db.Column(db.Text)
    escalafast2 = db.Column(db.Text)
    escalafast3 = db.Column(db.Text)
    escalafast4 = db.Column(db.Text)
    escalafast5 = db.Column(db.Text)
    escalafast6 = db.Column(db.Text)
    escalafast7 = db.Column(db.Text)
    escalafast8 = db.Column(db.Text)
    escalafast9 = db.Column(db.Text)
    escalafast10 = db.Column(db.Text)
    escalafast11 = db.Column(db.Text)
    escalafast12 = db.Column(db.Text)
    escalafast13 = db.Column(db.Text)
    escalafast14 = db.Column(db.Text)
    escalafast15 = db.Column(db.Text)
    escalafast16 = db.Column(db.Text)
    escalafast17 = db.Column(db.Text)
    escalafast18 = db.Column(db.Text)
    escalafast19 = db.Column(db.Text)
    escalafast20 = db.Column(db.Text)
    escalafast21 = db.Column(db.Text)
    escalafast22 = db.Column(db.Text)
    escalafast23 = db.Column(db.Text)
    escalafast24 = db.Column(db.Text)



class Escalawhoqoldepresionestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalawhoqol1 = db.Column(db.Text)
    escalawhoqol2 = db.Column(db.Text)
    escalawhoqol3 = db.Column(db.Text)
    escalawhoqol4 = db.Column(db.Text)
    escalawhoqol5 = db.Column(db.Text)
    escalawhoqol6 = db.Column(db.Text)
    escalawhoqol7 = db.Column(db.Text)
    escalawhoqol8 = db.Column(db.Text)
    escalawhoqol9 = db.Column(db.Text)
    escalawhoqol10 = db.Column(db.Text)
    escalawhoqol11 = db.Column(db.Text)
    escalawhoqol12 = db.Column(db.Text)
    escalawhoqol13 = db.Column(db.Text)
    escalawhoqol14 = db.Column(db.Text)
    escalawhoqol15 = db.Column(db.Text)
    escalawhoqol16 = db.Column(db.Text)
    escalawhoqol17 = db.Column(db.Text)
    escalawhoqol18 = db.Column(db.Text)
    escalawhoqol19 = db.Column(db.Text)
    escalawhoqol20 = db.Column(db.Text)
    escalawhoqol21 = db.Column(db.Text)
    escalawhoqol22 = db.Column(db.Text)
    escalawhoqol23 = db.Column(db.Text)
    escalawhoqol24 = db.Column(db.Text)
    escalawhoqol25 = db.Column(db.Text)
    escalawhoqol26 = db.Column(db.Text)
    escalawhoqol27 = db.Column(db.Text)
    escalawhoqol28 = db.Column(db.Text)
    escalawhoqol29 = db.Column(db.Text)



class Escalaeeagdepresionestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaeeag1 = db.Column(db.Text)



class Cuestionarioavataresdepresionestable(db.Model):
    __bind_key__ = 'datosdepresion'
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



class Appcaraspantalladepresionestable(db.Model):
    __bind_key__ = 'datosdepresion'
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
    


class Appcarasvrdepresionestable(db.Model):
    __bind_key__ = 'datosdepresion'
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


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Tabla datos paciente con depresion en estado inestable

class Escalaminicertsdepresioninestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaminicerts1 = db.Column(db.Text)
    escalaminicerts2 = db.Column(db.Text)
    escalaminicerts3 = db.Column(db.Text)
    escalaminicerts4 = db.Column(db.Text)
    escalaminicerts5 = db.Column(db.Text)
    escalaminicerts6 = db.Column(db.Text)
    escalaminicerts7 = db.Column(db.Text)
    escalaminicerts8 = db.Column(db.Text)
    escalaminicerts9 = db.Column(db.Text)
    escalaminicerts10 = db.Column(db.Text)
    escalaminicerts11 = db.Column(db.Text)
    escalaminicerts12 = db.Column(db.Text)
    escalaminicerts13 = db.Column(db.Text)
    escalaminicerts14 = db.Column(db.Text)
    escalaminicerts15 = db.Column(db.Text)
    escalaminicerts16 = db.Column(db.Text)


class Escalaius12depresioninestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaius12_1 = db.Column(db.Text)
    escalaius12_2 = db.Column(db.Text)
    escalaius12_3 = db.Column(db.Text)
    escalaius12_4 = db.Column(db.Text)
    escalaius12_5 = db.Column(db.Text)
    escalaius12_6 = db.Column(db.Text)
    escalaius12_7 = db.Column(db.Text)
    escalaius12_8 = db.Column(db.Text)
    escalaius12_9 = db.Column(db.Text)
    escalaius12_10 = db.Column(db.Text)
    escalaius12_11 = db.Column(db.Text)
    escalaius12_12 = db.Column(db.Text)



class Escalaebrddepresioninestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaebrd1 = db.Column(db.Text)
    escalaebrd2 = db.Column(db.Text)
    escalaebrd3 = db.Column(db.Text)
    escalaebrd4 = db.Column(db.Text)


class Escalabdiiidepresioninestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalabdiii1 = db.Column(db.Text)
    escalabdiii2 = db.Column(db.Text)
    escalabdiii3 = db.Column(db.Text)
    escalabdiii4 = db.Column(db.Text)
    escalabdiii5 = db.Column(db.Text)
    escalabdiii6 = db.Column(db.Text)
    escalabdiii7 = db.Column(db.Text)
    escalabdiii8 = db.Column(db.Text)
    escalabdiii9 = db.Column(db.Text)
    escalabdiii10 = db.Column(db.Text)
    escalabdiii11 = db.Column(db.Text)
    escalabdiii12 = db.Column(db.Text)
    escalabdiii13 = db.Column(db.Text)
    escalabdiii14 = db.Column(db.Text)
    escalabdiii15 = db.Column(db.Text)
    escalabdiii16 = db.Column(db.Text)
    escalabdiii17 = db.Column(db.Text)
    escalabdiii18 = db.Column(db.Text)
    escalabdiii19 = db.Column(db.Text)
    escalabdiii20 = db.Column(db.Text)
    escalabdiii21 = db.Column(db.Text)



class Escalashortstairdepresioninestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalashortstair1 = db.Column(db.Text)
    escalashortstair2 = db.Column(db.Text)
    escalashortstair3 = db.Column(db.Text)
    escalashortstair4 = db.Column(db.Text)
    escalashortstair5 = db.Column(db.Text)
    escalashortstair6 = db.Column(db.Text)
    escalashortstair7 = db.Column(db.Text)
    escalashortstair8 = db.Column(db.Text)


class Escalahrsddepresioninestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalahrsd1 = db.Column(db.Text)
    escalahrsd2 = db.Column(db.Text)
    escalahrsd3 = db.Column(db.Text)
    escalahrsd4 = db.Column(db.Text)
    escalahrsd5 = db.Column(db.Text)
    escalahrsd6 = db.Column(db.Text)
    escalahrsd7 = db.Column(db.Text)
    escalahrsd8 = db.Column(db.Text)
    escalahrsd9 = db.Column(db.Text)
    escalahrsd10 = db.Column(db.Text)
    escalahrsd11 = db.Column(db.Text)
    escalahrsd12 = db.Column(db.Text)
    escalahrsd13 = db.Column(db.Text)
    escalahrsd14 = db.Column(db.Text)
    escalahrsd15 = db.Column(db.Text)
    escalahrsd16 = db.Column(db.Text)
    escalahrsd17 = db.Column(db.Text)



class Escalapanasdepresioninestable(db.Model):
    __bind_key__ = 'datosdepresion'
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



class Escalafastdepresioninestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalafast1 = db.Column(db.Text)
    escalafast2 = db.Column(db.Text)
    escalafast3 = db.Column(db.Text)
    escalafast4 = db.Column(db.Text)
    escalafast5 = db.Column(db.Text)
    escalafast6 = db.Column(db.Text)
    escalafast7 = db.Column(db.Text)
    escalafast8 = db.Column(db.Text)
    escalafast9 = db.Column(db.Text)
    escalafast10 = db.Column(db.Text)
    escalafast11 = db.Column(db.Text)
    escalafast12 = db.Column(db.Text)
    escalafast13 = db.Column(db.Text)
    escalafast14 = db.Column(db.Text)
    escalafast15 = db.Column(db.Text)
    escalafast16 = db.Column(db.Text)
    escalafast17 = db.Column(db.Text)
    escalafast18 = db.Column(db.Text)
    escalafast19 = db.Column(db.Text)
    escalafast20 = db.Column(db.Text)
    escalafast21 = db.Column(db.Text)
    escalafast22 = db.Column(db.Text)
    escalafast23 = db.Column(db.Text)
    escalafast24 = db.Column(db.Text)



class Escalawhoqoldepresioninestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalawhoqol1 = db.Column(db.Text)
    escalawhoqol2 = db.Column(db.Text)
    escalawhoqol3 = db.Column(db.Text)
    escalawhoqol4 = db.Column(db.Text)
    escalawhoqol5 = db.Column(db.Text)
    escalawhoqol6 = db.Column(db.Text)
    escalawhoqol7 = db.Column(db.Text)
    escalawhoqol8 = db.Column(db.Text)
    escalawhoqol9 = db.Column(db.Text)
    escalawhoqol10 = db.Column(db.Text)
    escalawhoqol11 = db.Column(db.Text)
    escalawhoqol12 = db.Column(db.Text)
    escalawhoqol13 = db.Column(db.Text)
    escalawhoqol14 = db.Column(db.Text)
    escalawhoqol15 = db.Column(db.Text)
    escalawhoqol16 = db.Column(db.Text)
    escalawhoqol17 = db.Column(db.Text)
    escalawhoqol18 = db.Column(db.Text)
    escalawhoqol19 = db.Column(db.Text)
    escalawhoqol20 = db.Column(db.Text)
    escalawhoqol21 = db.Column(db.Text)
    escalawhoqol22 = db.Column(db.Text)
    escalawhoqol23 = db.Column(db.Text)
    escalawhoqol24 = db.Column(db.Text)
    escalawhoqol25 = db.Column(db.Text)
    escalawhoqol26 = db.Column(db.Text)
    escalawhoqol27 = db.Column(db.Text)
    escalawhoqol28 = db.Column(db.Text)
    escalawhoqol29 = db.Column(db.Text)



class Escalaeeagdepresioninestable(db.Model):
    __bind_key__ = 'datosdepresion'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaeeag1 = db.Column(db.Text)



class Cuestionarioavataresdepresioninestable(db.Model):
    __bind_key__ = 'datosdepresion'
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



class Appcaraspantalladepresioninestable(db.Model):
    __bind_key__ = 'datosdepresion'
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
    


class Appcarasvrdepresioninestable(db.Model):
    __bind_key__ = 'datosdepresion'
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

class Formularioantecedentesbipolarinestable(db.Model):
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

class Escalamadrsbipolarestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalamadrs1 = db.Column(db.Text)
    escalamadrs2 = db.Column(db.Text)
    escalamadrs3 = db.Column(db.Text)
    escalamadrs4 = db.Column(db.Text)
    escalamadrs5 = db.Column(db.Text)
    escalamadrs6 = db.Column(db.Text)
    escalamadrs7 = db.Column(db.Text)
    escalamadrs8 = db.Column(db.Text)
    escalamadrs9 = db.Column(db.Text)
    escalamadrs10 = db.Column(db.Text)



class Escalaymrsbipolarestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaymrs1 = db.Column(db.Text)
    escalaymrs2 = db.Column(db.Text)
    escalaymrs3 = db.Column(db.Text)
    escalaymrs4 = db.Column(db.Text)
    escalaymrs5 = db.Column(db.Text)
    escalaymrs6 = db.Column(db.Text)
    escalaymrs7 = db.Column(db.Text)
    escalaymrs8 = db.Column(db.Text)
    escalaymrs9 = db.Column(db.Text)
    escalaymrs10 = db.Column(db.Text)
    escalaymrs11 = db.Column(db.Text)



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



class Escalafastbipolarestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalafast1 = db.Column(db.Text)
    escalafast2 = db.Column(db.Text)
    escalafast3 = db.Column(db.Text)
    escalafast4 = db.Column(db.Text)
    escalafast5 = db.Column(db.Text)
    escalafast6 = db.Column(db.Text)
    escalafast7 = db.Column(db.Text)
    escalafast8 = db.Column(db.Text)
    escalafast9 = db.Column(db.Text)
    escalafast10 = db.Column(db.Text)
    escalafast11 = db.Column(db.Text)
    escalafast12 = db.Column(db.Text)
    escalafast13 = db.Column(db.Text)
    escalafast14 = db.Column(db.Text)
    escalafast15 = db.Column(db.Text)
    escalafast16 = db.Column(db.Text)
    escalafast17 = db.Column(db.Text)
    escalafast18 = db.Column(db.Text)
    escalafast19 = db.Column(db.Text)
    escalafast20 = db.Column(db.Text)
    escalafast21 = db.Column(db.Text)
    escalafast22 = db.Column(db.Text)
    escalafast23 = db.Column(db.Text)
    escalafast24 = db.Column(db.Text)



class Escalawhoqolbipolarestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalawhoqol1 = db.Column(db.Text)
    escalawhoqol2 = db.Column(db.Text)
    escalawhoqol3 = db.Column(db.Text)
    escalawhoqol4 = db.Column(db.Text)
    escalawhoqol5 = db.Column(db.Text)
    escalawhoqol6 = db.Column(db.Text)
    escalawhoqol7 = db.Column(db.Text)
    escalawhoqol8 = db.Column(db.Text)
    escalawhoqol9 = db.Column(db.Text)
    escalawhoqol10 = db.Column(db.Text)
    escalawhoqol11 = db.Column(db.Text)
    escalawhoqol12 = db.Column(db.Text)
    escalawhoqol13 = db.Column(db.Text)
    escalawhoqol14 = db.Column(db.Text)
    escalawhoqol15 = db.Column(db.Text)
    escalawhoqol16 = db.Column(db.Text)
    escalawhoqol17 = db.Column(db.Text)
    escalawhoqol18 = db.Column(db.Text)
    escalawhoqol19 = db.Column(db.Text)
    escalawhoqol20 = db.Column(db.Text)
    escalawhoqol21 = db.Column(db.Text)
    escalawhoqol22 = db.Column(db.Text)
    escalawhoqol23 = db.Column(db.Text)
    escalawhoqol24 = db.Column(db.Text)
    escalawhoqol25 = db.Column(db.Text)
    escalawhoqol26 = db.Column(db.Text)
    escalawhoqol27 = db.Column(db.Text)
    escalawhoqol28 = db.Column(db.Text)
    escalawhoqol29 = db.Column(db.Text)



class Escalaeeagbipolarestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaeeag1 = db.Column(db.Text)



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


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Tabla datos paciente bipolar en estado inestable

class Escalamadrsbipolarinestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalamadrs1 = db.Column(db.Text)
    escalamadrs2 = db.Column(db.Text)
    escalamadrs3 = db.Column(db.Text)
    escalamadrs4 = db.Column(db.Text)
    escalamadrs5 = db.Column(db.Text)
    escalamadrs6 = db.Column(db.Text)
    escalamadrs7 = db.Column(db.Text)
    escalamadrs8 = db.Column(db.Text)
    escalamadrs9 = db.Column(db.Text)
    escalamadrs10 = db.Column(db.Text)



class Escalaymrsbipolarinestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaymrs1 = db.Column(db.Text)
    escalaymrs2 = db.Column(db.Text)
    escalaymrs3 = db.Column(db.Text)
    escalaymrs4 = db.Column(db.Text)
    escalaymrs5 = db.Column(db.Text)
    escalaymrs6 = db.Column(db.Text)
    escalaymrs7 = db.Column(db.Text)
    escalaymrs8 = db.Column(db.Text)
    escalaymrs9 = db.Column(db.Text)
    escalaymrs10 = db.Column(db.Text)
    escalaymrs11 = db.Column(db.Text)



class Escalapanasbipolarinestable(db.Model):
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



class Escalafastbipolarinestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalafast1 = db.Column(db.Text)
    escalafast2 = db.Column(db.Text)
    escalafast3 = db.Column(db.Text)
    escalafast4 = db.Column(db.Text)
    escalafast5 = db.Column(db.Text)
    escalafast6 = db.Column(db.Text)
    escalafast7 = db.Column(db.Text)
    escalafast8 = db.Column(db.Text)
    escalafast9 = db.Column(db.Text)
    escalafast10 = db.Column(db.Text)
    escalafast11 = db.Column(db.Text)
    escalafast12 = db.Column(db.Text)
    escalafast13 = db.Column(db.Text)
    escalafast14 = db.Column(db.Text)
    escalafast15 = db.Column(db.Text)
    escalafast16 = db.Column(db.Text)
    escalafast17 = db.Column(db.Text)
    escalafast18 = db.Column(db.Text)
    escalafast19 = db.Column(db.Text)
    escalafast20 = db.Column(db.Text)
    escalafast21 = db.Column(db.Text)
    escalafast22 = db.Column(db.Text)
    escalafast23 = db.Column(db.Text)
    escalafast24 = db.Column(db.Text)



class Escalawhoqolbipolarinestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalawhoqol1 = db.Column(db.Text)
    escalawhoqol2 = db.Column(db.Text)
    escalawhoqol3 = db.Column(db.Text)
    escalawhoqol4 = db.Column(db.Text)
    escalawhoqol5 = db.Column(db.Text)
    escalawhoqol6 = db.Column(db.Text)
    escalawhoqol7 = db.Column(db.Text)
    escalawhoqol8 = db.Column(db.Text)
    escalawhoqol9 = db.Column(db.Text)
    escalawhoqol10 = db.Column(db.Text)
    escalawhoqol11 = db.Column(db.Text)
    escalawhoqol12 = db.Column(db.Text)
    escalawhoqol13 = db.Column(db.Text)
    escalawhoqol14 = db.Column(db.Text)
    escalawhoqol15 = db.Column(db.Text)
    escalawhoqol16 = db.Column(db.Text)
    escalawhoqol17 = db.Column(db.Text)
    escalawhoqol18 = db.Column(db.Text)
    escalawhoqol19 = db.Column(db.Text)
    escalawhoqol20 = db.Column(db.Text)
    escalawhoqol21 = db.Column(db.Text)
    escalawhoqol22 = db.Column(db.Text)
    escalawhoqol23 = db.Column(db.Text)
    escalawhoqol24 = db.Column(db.Text)
    escalawhoqol25 = db.Column(db.Text)
    escalawhoqol26 = db.Column(db.Text)
    escalawhoqol27 = db.Column(db.Text)
    escalawhoqol28 = db.Column(db.Text)
    escalawhoqol29 = db.Column(db.Text)



class Escalaeeagbipolarinestable(db.Model):
    __bind_key__ = 'datosbipolar'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaeeag1 = db.Column(db.Text)



class Cuestionarioavataresbipolarinestable(db.Model):
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



class Appcaraspantallabipolarinestable(db.Model):
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
    
    

class Appcarasvrbipolarinestable(db.Model):
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



# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Tabla datos formulario para paciente con esquizofrenia

class Formularioregistroesquizofrenia(db.Model):
    __bind_key__ = 'datosesquizofrenia'
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


# Tabla datos formulario secundario para paciente con esquizofrenia (cantidad 2)

class Formularioantecedentesesquizofreniaestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    # datos antecedentes personales somáticos para paciente con esquizofrenia
    antecedentespersonalessomaticos = db.Column(db.Text)
    
    # datos antecedentes personales psiquiatricos para paciente con esquizofrenia
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


class Formularioantecedentesesquizofreniainestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    # datos antecedentes personales somáticos para paciente con esquizofrenia
    antecedentespersonalessomaticos = db.Column(db.Text)
    
    # datos antecedentes personales psiquiatricos para paciente con esquizofrenia
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

# Tabla datos paciente con esquizofrenia en estado estable

class Escalapanssesquizofreniaestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalapanss1 = db.Column(db.Text)
    escalapanss2 = db.Column(db.Text)
    escalapanss3 = db.Column(db.Text)
    escalapanss4 = db.Column(db.Text)
    escalapanss5 = db.Column(db.Text)
    escalapanss6 = db.Column(db.Text)
    escalapanss7 = db.Column(db.Text)
    escalapanss8 = db.Column(db.Text)
    escalapanss9 = db.Column(db.Text)
    escalapanss10 = db.Column(db.Text)
    escalapanss11 = db.Column(db.Text)
    escalapanss12 = db.Column(db.Text)
    escalapanss13 = db.Column(db.Text)
    escalapanss14 = db.Column(db.Text)
    escalapanss15 = db.Column(db.Text)
    escalapanss16 = db.Column(db.Text)
    escalapanss17 = db.Column(db.Text)
    escalapanss18 = db.Column(db.Text)
    escalapanss19 = db.Column(db.Text)
    escalapanss20 = db.Column(db.Text)
    escalapanss21 = db.Column(db.Text)
    escalapanss22 = db.Column(db.Text)
    escalapanss23 = db.Column(db.Text)
    escalapanss24 = db.Column(db.Text)
    escalapanss25 = db.Column(db.Text)
    escalapanss26 = db.Column(db.Text)
    escalapanss27 = db.Column(db.Text)
    escalapanss28 = db.Column(db.Text)
    escalapanss29 = db.Column(db.Text)
    escalapanss30 = db.Column(db.Text)



class Escalapanasesquizofreniaestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
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



class Escalafastesquizofreniaestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalafast1 = db.Column(db.Text)
    escalafast2 = db.Column(db.Text)
    escalafast3 = db.Column(db.Text)
    escalafast4 = db.Column(db.Text)
    escalafast5 = db.Column(db.Text)
    escalafast6 = db.Column(db.Text)
    escalafast7 = db.Column(db.Text)
    escalafast8 = db.Column(db.Text)
    escalafast9 = db.Column(db.Text)
    escalafast10 = db.Column(db.Text)
    escalafast11 = db.Column(db.Text)
    escalafast12 = db.Column(db.Text)
    escalafast13 = db.Column(db.Text)
    escalafast14 = db.Column(db.Text)
    escalafast15 = db.Column(db.Text)
    escalafast16 = db.Column(db.Text)
    escalafast17 = db.Column(db.Text)
    escalafast18 = db.Column(db.Text)
    escalafast19 = db.Column(db.Text)
    escalafast20 = db.Column(db.Text)
    escalafast21 = db.Column(db.Text)
    escalafast22 = db.Column(db.Text)
    escalafast23 = db.Column(db.Text)
    escalafast24 = db.Column(db.Text)



class Escalawhoqolesquizofreniaestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalawhoqol1 = db.Column(db.Text)
    escalawhoqol2 = db.Column(db.Text)
    escalawhoqol3 = db.Column(db.Text)
    escalawhoqol4 = db.Column(db.Text)
    escalawhoqol5 = db.Column(db.Text)
    escalawhoqol6 = db.Column(db.Text)
    escalawhoqol7 = db.Column(db.Text)
    escalawhoqol8 = db.Column(db.Text)
    escalawhoqol9 = db.Column(db.Text)
    escalawhoqol10 = db.Column(db.Text)
    escalawhoqol11 = db.Column(db.Text)
    escalawhoqol12 = db.Column(db.Text)
    escalawhoqol13 = db.Column(db.Text)
    escalawhoqol14 = db.Column(db.Text)
    escalawhoqol15 = db.Column(db.Text)
    escalawhoqol16 = db.Column(db.Text)
    escalawhoqol17 = db.Column(db.Text)
    escalawhoqol18 = db.Column(db.Text)
    escalawhoqol19 = db.Column(db.Text)
    escalawhoqol20 = db.Column(db.Text)
    escalawhoqol21 = db.Column(db.Text)
    escalawhoqol22 = db.Column(db.Text)
    escalawhoqol23 = db.Column(db.Text)
    escalawhoqol24 = db.Column(db.Text)
    escalawhoqol25 = db.Column(db.Text)
    escalawhoqol26 = db.Column(db.Text)
    escalawhoqol27 = db.Column(db.Text)
    escalawhoqol28 = db.Column(db.Text)
    escalawhoqol29 = db.Column(db.Text)



class Escalaeeagesquizofreniaestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaeeag1 = db.Column(db.Text)



class Cuestionarioavataresesquizofreniaestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
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



class Appcaraspantallaesquizofreniaestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
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
    


class Appcarasvresquizofreniaestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
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



# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Tabla datos paciente con esquizofrenia en estado inestable

class Escalapanssesquizofreniainestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalapanss1 = db.Column(db.Text)
    escalapanss2 = db.Column(db.Text)
    escalapanss3 = db.Column(db.Text)
    escalapanss4 = db.Column(db.Text)
    escalapanss5 = db.Column(db.Text)
    escalapanss6 = db.Column(db.Text)
    escalapanss7 = db.Column(db.Text)
    escalapanss8 = db.Column(db.Text)
    escalapanss9 = db.Column(db.Text)
    escalapanss10 = db.Column(db.Text)
    escalapanss11 = db.Column(db.Text)
    escalapanss12 = db.Column(db.Text)
    escalapanss13 = db.Column(db.Text)
    escalapanss14 = db.Column(db.Text)
    escalapanss15 = db.Column(db.Text)
    escalapanss16 = db.Column(db.Text)
    escalapanss17 = db.Column(db.Text)
    escalapanss18 = db.Column(db.Text)
    escalapanss19 = db.Column(db.Text)
    escalapanss20 = db.Column(db.Text)
    escalapanss21 = db.Column(db.Text)
    escalapanss22 = db.Column(db.Text)
    escalapanss23 = db.Column(db.Text)
    escalapanss24 = db.Column(db.Text)
    escalapanss25 = db.Column(db.Text)
    escalapanss26 = db.Column(db.Text)
    escalapanss27 = db.Column(db.Text)
    escalapanss28 = db.Column(db.Text)
    escalapanss29 = db.Column(db.Text)
    escalapanss30 = db.Column(db.Text)



class Escalapanasesquizofreniainestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
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



class Escalafastesquizofreniainestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalafast1 = db.Column(db.Text)
    escalafast2 = db.Column(db.Text)
    escalafast3 = db.Column(db.Text)
    escalafast4 = db.Column(db.Text)
    escalafast5 = db.Column(db.Text)
    escalafast6 = db.Column(db.Text)
    escalafast7 = db.Column(db.Text)
    escalafast8 = db.Column(db.Text)
    escalafast9 = db.Column(db.Text)
    escalafast10 = db.Column(db.Text)
    escalafast11 = db.Column(db.Text)
    escalafast12 = db.Column(db.Text)
    escalafast13 = db.Column(db.Text)
    escalafast14 = db.Column(db.Text)
    escalafast15 = db.Column(db.Text)
    escalafast16 = db.Column(db.Text)
    escalafast17 = db.Column(db.Text)
    escalafast18 = db.Column(db.Text)
    escalafast19 = db.Column(db.Text)
    escalafast20 = db.Column(db.Text)
    escalafast21 = db.Column(db.Text)
    escalafast22 = db.Column(db.Text)
    escalafast23 = db.Column(db.Text)
    escalafast24 = db.Column(db.Text)



class Escalawhoqolesquizofreniainestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalawhoqol1 = db.Column(db.Text)
    escalawhoqol2 = db.Column(db.Text)
    escalawhoqol3 = db.Column(db.Text)
    escalawhoqol4 = db.Column(db.Text)
    escalawhoqol5 = db.Column(db.Text)
    escalawhoqol6 = db.Column(db.Text)
    escalawhoqol7 = db.Column(db.Text)
    escalawhoqol8 = db.Column(db.Text)
    escalawhoqol9 = db.Column(db.Text)
    escalawhoqol10 = db.Column(db.Text)
    escalawhoqol11 = db.Column(db.Text)
    escalawhoqol12 = db.Column(db.Text)
    escalawhoqol13 = db.Column(db.Text)
    escalawhoqol14 = db.Column(db.Text)
    escalawhoqol15 = db.Column(db.Text)
    escalawhoqol16 = db.Column(db.Text)
    escalawhoqol17 = db.Column(db.Text)
    escalawhoqol18 = db.Column(db.Text)
    escalawhoqol19 = db.Column(db.Text)
    escalawhoqol20 = db.Column(db.Text)
    escalawhoqol21 = db.Column(db.Text)
    escalawhoqol22 = db.Column(db.Text)
    escalawhoqol23 = db.Column(db.Text)
    escalawhoqol24 = db.Column(db.Text)
    escalawhoqol25 = db.Column(db.Text)
    escalawhoqol26 = db.Column(db.Text)
    escalawhoqol27 = db.Column(db.Text)
    escalawhoqol28 = db.Column(db.Text)
    escalawhoqol29 = db.Column(db.Text)



class Escalaeeagesquizofreniainestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaeeag1 = db.Column(db.Text)



class Cuestionarioavataresesquizofreniainestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
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



class Appcaraspantallaesquizofreniainestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
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
    


class Appcarasvresquizofreniainestable(db.Model):
    __bind_key__ = 'datosesquizofrenia'
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





















# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Tabla datos formulario para paciente esquizoafectivo

class Formularioregistroesquizoafectivo(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
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
    antecedentespersonalessomaticos = db.Column(db.Text)



# Tabla datos formulario secundario para paciente con esquizoafectivo

class Formularioantecedentesesquizoafectivoestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    # datos antecedentes personales somáticos para paciente esquizoafectivo 
    antecedentespersonalessomaticos = db.Column(db.Text)
    
    # datos antecedentes personales psiquiatricos para paciente esquizoafectivo
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


class Formularioantecedentesesquizoafectivoinestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    # datos antecedentes personales somáticos para paciente esquizoafectivo 
    antecedentespersonalessomaticos = db.Column(db.Text)
    
    # datos antecedentes personales psiquiatricos para paciente esquizoafectivo
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

# Tabla datos paciente esquizoafectivo en estado estable

class Escalapanssesquizoafectivoestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalapanss1 = db.Column(db.Text)
    escalapanss2 = db.Column(db.Text)
    escalapanss3 = db.Column(db.Text)
    escalapanss4 = db.Column(db.Text)
    escalapanss5 = db.Column(db.Text)
    escalapanss6 = db.Column(db.Text)
    escalapanss7 = db.Column(db.Text)
    escalapanss8 = db.Column(db.Text)
    escalapanss9 = db.Column(db.Text)
    escalapanss10 = db.Column(db.Text)
    escalapanss11 = db.Column(db.Text)
    escalapanss12 = db.Column(db.Text)
    escalapanss13 = db.Column(db.Text)
    escalapanss14 = db.Column(db.Text)
    escalapanss15 = db.Column(db.Text)
    escalapanss16 = db.Column(db.Text)
    escalapanss17 = db.Column(db.Text)
    escalapanss18 = db.Column(db.Text)
    escalapanss19 = db.Column(db.Text)
    escalapanss20 = db.Column(db.Text)
    escalapanss21 = db.Column(db.Text)
    escalapanss22 = db.Column(db.Text)
    escalapanss23 = db.Column(db.Text)
    escalapanss24 = db.Column(db.Text)
    escalapanss25 = db.Column(db.Text)
    escalapanss26 = db.Column(db.Text)
    escalapanss27 = db.Column(db.Text)
    escalapanss28 = db.Column(db.Text)
    escalapanss29 = db.Column(db.Text)
    escalapanss30 = db.Column(db.Text)



class Escalamadrsesquizoafectivoestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalamadrs1 = db.Column(db.Text)
    escalamadrs2 = db.Column(db.Text)
    escalamadrs3 = db.Column(db.Text)
    escalamadrs4 = db.Column(db.Text)
    escalamadrs5 = db.Column(db.Text)
    escalamadrs6 = db.Column(db.Text)
    escalamadrs7 = db.Column(db.Text)
    escalamadrs8 = db.Column(db.Text)
    escalamadrs9 = db.Column(db.Text)
    escalamadrs10 = db.Column(db.Text)



class Escalaymrsesquizoafectivoestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaymrs1 = db.Column(db.Text)
    escalaymrs2 = db.Column(db.Text)
    escalaymrs3 = db.Column(db.Text)
    escalaymrs4 = db.Column(db.Text)
    escalaymrs5 = db.Column(db.Text)
    escalaymrs6 = db.Column(db.Text)
    escalaymrs7 = db.Column(db.Text)
    escalaymrs8 = db.Column(db.Text)
    escalaymrs9 = db.Column(db.Text)
    escalaymrs10 = db.Column(db.Text)
    escalaymrs11 = db.Column(db.Text)



class Escalapanasesquizoafectivoestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
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



class Escalafastesquizoafectivoestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalafast1 = db.Column(db.Text)
    escalafast2 = db.Column(db.Text)
    escalafast3 = db.Column(db.Text)
    escalafast4 = db.Column(db.Text)
    escalafast5 = db.Column(db.Text)
    escalafast6 = db.Column(db.Text)
    escalafast7 = db.Column(db.Text)
    escalafast8 = db.Column(db.Text)
    escalafast9 = db.Column(db.Text)
    escalafast10 = db.Column(db.Text)
    escalafast11 = db.Column(db.Text)
    escalafast12 = db.Column(db.Text)
    escalafast13 = db.Column(db.Text)
    escalafast14 = db.Column(db.Text)
    escalafast15 = db.Column(db.Text)
    escalafast16 = db.Column(db.Text)
    escalafast17 = db.Column(db.Text)
    escalafast18 = db.Column(db.Text)
    escalafast19 = db.Column(db.Text)
    escalafast20 = db.Column(db.Text)
    escalafast21 = db.Column(db.Text)
    escalafast22 = db.Column(db.Text)
    escalafast23 = db.Column(db.Text)
    escalafast24 = db.Column(db.Text)



class Escalawhoqolesquizoafectivoestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalawhoqol1 = db.Column(db.Text)
    escalawhoqol2 = db.Column(db.Text)
    escalawhoqol3 = db.Column(db.Text)
    escalawhoqol4 = db.Column(db.Text)
    escalawhoqol5 = db.Column(db.Text)
    escalawhoqol6 = db.Column(db.Text)
    escalawhoqol7 = db.Column(db.Text)
    escalawhoqol8 = db.Column(db.Text)
    escalawhoqol9 = db.Column(db.Text)
    escalawhoqol10 = db.Column(db.Text)
    escalawhoqol11 = db.Column(db.Text)
    escalawhoqol12 = db.Column(db.Text)
    escalawhoqol13 = db.Column(db.Text)
    escalawhoqol14 = db.Column(db.Text)
    escalawhoqol15 = db.Column(db.Text)
    escalawhoqol16 = db.Column(db.Text)
    escalawhoqol17 = db.Column(db.Text)
    escalawhoqol18 = db.Column(db.Text)
    escalawhoqol19 = db.Column(db.Text)
    escalawhoqol20 = db.Column(db.Text)
    escalawhoqol21 = db.Column(db.Text)
    escalawhoqol22 = db.Column(db.Text)
    escalawhoqol23 = db.Column(db.Text)
    escalawhoqol24 = db.Column(db.Text)
    escalawhoqol25 = db.Column(db.Text)
    escalawhoqol26 = db.Column(db.Text)
    escalawhoqol27 = db.Column(db.Text)
    escalawhoqol28 = db.Column(db.Text)
    escalawhoqol29 = db.Column(db.Text)



class Escalaeeagesquizoafectivoestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaeeag1 = db.Column(db.Text)



class Cuestionarioavataresesquizoafectivoestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
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



class Appcaraspantallaesquizoafectivoestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
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
    


class Appcarasvresquizoafectivoestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
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


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Tabla datos paciente esquizoafectivo en estado inestable

class Escalapanssesquizoafectivoinestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalapanss1 = db.Column(db.Text)
    escalapanss2 = db.Column(db.Text)
    escalapanss3 = db.Column(db.Text)
    escalapanss4 = db.Column(db.Text)
    escalapanss5 = db.Column(db.Text)
    escalapanss6 = db.Column(db.Text)
    escalapanss7 = db.Column(db.Text)
    escalapanss8 = db.Column(db.Text)
    escalapanss9 = db.Column(db.Text)
    escalapanss10 = db.Column(db.Text)
    escalapanss11 = db.Column(db.Text)
    escalapanss12 = db.Column(db.Text)
    escalapanss13 = db.Column(db.Text)
    escalapanss14 = db.Column(db.Text)
    escalapanss15 = db.Column(db.Text)
    escalapanss16 = db.Column(db.Text)
    escalapanss17 = db.Column(db.Text)
    escalapanss18 = db.Column(db.Text)
    escalapanss19 = db.Column(db.Text)
    escalapanss20 = db.Column(db.Text)
    escalapanss21 = db.Column(db.Text)
    escalapanss22 = db.Column(db.Text)
    escalapanss23 = db.Column(db.Text)
    escalapanss24 = db.Column(db.Text)
    escalapanss25 = db.Column(db.Text)
    escalapanss26 = db.Column(db.Text)
    escalapanss27 = db.Column(db.Text)
    escalapanss28 = db.Column(db.Text)
    escalapanss29 = db.Column(db.Text)
    escalapanss30 = db.Column(db.Text)



class Escalamadrsesquizoafectivoinestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalamadrs1 = db.Column(db.Text)
    escalamadrs2 = db.Column(db.Text)
    escalamadrs3 = db.Column(db.Text)
    escalamadrs4 = db.Column(db.Text)
    escalamadrs5 = db.Column(db.Text)
    escalamadrs6 = db.Column(db.Text)
    escalamadrs7 = db.Column(db.Text)
    escalamadrs8 = db.Column(db.Text)
    escalamadrs9 = db.Column(db.Text)
    escalamadrs10 = db.Column(db.Text)



class Escalaymrsesquizoafectivoinestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaymrs1 = db.Column(db.Text)
    escalaymrs2 = db.Column(db.Text)
    escalaymrs3 = db.Column(db.Text)
    escalaymrs4 = db.Column(db.Text)
    escalaymrs5 = db.Column(db.Text)
    escalaymrs6 = db.Column(db.Text)
    escalaymrs7 = db.Column(db.Text)
    escalaymrs8 = db.Column(db.Text)
    escalaymrs9 = db.Column(db.Text)
    escalaymrs10 = db.Column(db.Text)
    escalaymrs11 = db.Column(db.Text)



class Escalapanasesquizoafectivoinestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
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



class Escalafastesquizoafectivoinestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalafast1 = db.Column(db.Text)
    escalafast2 = db.Column(db.Text)
    escalafast3 = db.Column(db.Text)
    escalafast4 = db.Column(db.Text)
    escalafast5 = db.Column(db.Text)
    escalafast6 = db.Column(db.Text)
    escalafast7 = db.Column(db.Text)
    escalafast8 = db.Column(db.Text)
    escalafast9 = db.Column(db.Text)
    escalafast10 = db.Column(db.Text)
    escalafast11 = db.Column(db.Text)
    escalafast12 = db.Column(db.Text)
    escalafast13 = db.Column(db.Text)
    escalafast14 = db.Column(db.Text)
    escalafast15 = db.Column(db.Text)
    escalafast16 = db.Column(db.Text)
    escalafast17 = db.Column(db.Text)
    escalafast18 = db.Column(db.Text)
    escalafast19 = db.Column(db.Text)
    escalafast20 = db.Column(db.Text)
    escalafast21 = db.Column(db.Text)
    escalafast22 = db.Column(db.Text)
    escalafast23 = db.Column(db.Text)
    escalafast24 = db.Column(db.Text)



class Escalawhoqolesquizoafectivoinestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalawhoqol1 = db.Column(db.Text)
    escalawhoqol2 = db.Column(db.Text)
    escalawhoqol3 = db.Column(db.Text)
    escalawhoqol4 = db.Column(db.Text)
    escalawhoqol5 = db.Column(db.Text)
    escalawhoqol6 = db.Column(db.Text)
    escalawhoqol7 = db.Column(db.Text)
    escalawhoqol8 = db.Column(db.Text)
    escalawhoqol9 = db.Column(db.Text)
    escalawhoqol10 = db.Column(db.Text)
    escalawhoqol11 = db.Column(db.Text)
    escalawhoqol12 = db.Column(db.Text)
    escalawhoqol13 = db.Column(db.Text)
    escalawhoqol14 = db.Column(db.Text)
    escalawhoqol15 = db.Column(db.Text)
    escalawhoqol16 = db.Column(db.Text)
    escalawhoqol17 = db.Column(db.Text)
    escalawhoqol18 = db.Column(db.Text)
    escalawhoqol19 = db.Column(db.Text)
    escalawhoqol20 = db.Column(db.Text)
    escalawhoqol21 = db.Column(db.Text)
    escalawhoqol22 = db.Column(db.Text)
    escalawhoqol23 = db.Column(db.Text)
    escalawhoqol24 = db.Column(db.Text)
    escalawhoqol25 = db.Column(db.Text)
    escalawhoqol26 = db.Column(db.Text)
    escalawhoqol27 = db.Column(db.Text)
    escalawhoqol28 = db.Column(db.Text)
    escalawhoqol29 = db.Column(db.Text)



class Escalaeeagesquizoafectivoinestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
    idescala = db.Column(db.Integer, primary_key=True)
    
    idpaciente = db.Column(db.Text)
    nhcpaciente = db.Column(db.Text)

    tipopaciente = db.Column(db.Text)
    estadopaciente = db.Column(db.Text)
    estadoescala = db.Column(db.Text)
    
    fechacreacion = db.Column(db.Text)
    fechaultimamodificacion = db.Column(db.Text)

    escalaeeag1 = db.Column(db.Text)



class Cuestionarioavataresesquizoafectivoinestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
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



class Appcaraspantallaesquizoafectivoinestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
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
    


class Appcarasvresquizoafectivoinestable(db.Model):
    __bind_key__ = 'datosesquizoafectivo'
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

@appcarasestableinestable.route("/", methods=["GET", "POST"])
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

@appcarasestableinestable.route("/listapacientes/<string:tipopaciente>/", methods=["GET", "POST"])
def listapacientes(tipopaciente=""):

    if tipopaciente == "depresion":
        nombretablabd = Formularioregistrodepresion
        tipolayout = 'layoutinicio2.html'
    
    elif tipopaciente == "bipolar":
        nombretablabd = Formularioregistrobipolar
        tipolayout = 'layoutinicio2.html'
    
    elif tipopaciente == "esquizofrenia":
        nombretablabd = Formularioregistroesquizofrenia
        tipolayout = 'layoutinicio2.html'

    elif tipopaciente == "esquizoafectivo":
        nombretablabd = Formularioregistroesquizoafectivo
        tipolayout = 'layoutinicio2.html'
    
    # Para obtener todos los pacientes de registrados y mandarlos al html para generar la lista
    listapacientes = nombretablabd.query.all()
    numeropacientes = len(listapacientes)

    return render_template("listapacientes.html", tipolayout=tipolayout, tipopaciente=tipopaciente, listapacientes=listapacientes, numeropacientes=numeropacientes)



# fin pagina lista de pacientes ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////








# pagina lista formularios del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# para generar la lista de formularios secundarios y escalas del paciente, es decir, los formularios y escalas que pertenecen a cada paciente

@appcarasestableinestable.route("/listaformulariospaciente/<string:tipopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def listaformulariospaciente(tipopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':

        if request.form.get('salirpaciente') == "Salir del Paciente":
            
            return redirect(url_for('listapacientes', tipopaciente=tipopaciente))
    

    if tipopaciente == "depresion":
        # hay que pasar los datos de todas las formularios secundarios y escalas en su version estable e inestable (28 escalas)
        
        datosformularioantecedentesestable = buscarfirstpaciente(Formularioantecedentesdepresionestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalapanasestable = buscarfirstpaciente(Escalapanasdepresionestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalafastestable = buscarfirstpaciente(Escalafastdepresionestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalawhoqolestable = buscarfirstpaciente(Escalawhoqoldepresionestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalaeeagestable = buscarfirstpaciente(Escalaeeagdepresionestable, idpaciente, nhcpaciente, fechacreacion)
        datoscuestionarioavataresestable = buscarfirstpaciente(Cuestionarioavataresdepresionestable, idpaciente, nhcpaciente, fechacreacion)
        
        datosappcaraspantallaestable = buscarfirstpacienteappcaras(Appcaraspantalladepresionestable, idpaciente, nhcpaciente)
        datosappcarasvrestable = buscarfirstpacienteappcaras(Appcarasvrdepresionestable, idpaciente, nhcpaciente)


        datosescalaminicertsestable = buscarfirstpaciente(Escalaminicertsdepresionestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalaius12estable = buscarfirstpaciente(Escalaius12depresionestable, idpaciente, nhcpaciente, fechacreacion) 
        datosescalaebrdestable = buscarfirstpaciente(Escalaebrddepresionestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalabdiiiestable = buscarfirstpaciente(Escalabdiiidepresionestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalashortstairestable = buscarfirstpaciente(Escalashortstairdepresionestable, idpaciente, nhcpaciente, fechacreacion) 
        datosescalahrsdestable = buscarfirstpaciente(Escalahrsddepresionestable, idpaciente, nhcpaciente, fechacreacion)


        datosformularioantecedentesinestable = buscarfirstpaciente(Formularioantecedentesdepresioninestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalapanasinestable = buscarfirstpaciente(Escalapanasdepresioninestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalafastinestable = buscarfirstpaciente(Escalafastdepresioninestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalawhoqolinestable = buscarfirstpaciente(Escalawhoqoldepresioninestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalaeeaginestable = buscarfirstpaciente(Escalaeeagdepresioninestable, idpaciente, nhcpaciente, fechacreacion)
        datoscuestionarioavataresinestable = buscarfirstpaciente(Cuestionarioavataresdepresioninestable, idpaciente, nhcpaciente, fechacreacion)

        datosappcaraspantallainestable = buscarfirstpacienteappcaras(Appcaraspantalladepresioninestable, idpaciente, nhcpaciente)
        datosappcarasvrinestable = buscarfirstpacienteappcaras(Appcarasvrdepresioninestable, idpaciente, nhcpaciente)

        datosescalaminicertsinestable = buscarfirstpaciente(Escalaminicertsdepresioninestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalaius12inestable = buscarfirstpaciente(Escalaius12depresioninestable, idpaciente, nhcpaciente, fechacreacion) 
        datosescalaebrdinestable = buscarfirstpaciente(Escalaebrddepresioninestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalabdiiiinestable = buscarfirstpaciente(Escalabdiiidepresioninestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalashortstairinestable = buscarfirstpaciente(Escalashortstairdepresioninestable, idpaciente, nhcpaciente, fechacreacion) 
        datosescalahrsdinestable = buscarfirstpaciente(Escalahrsddepresioninestable, idpaciente, nhcpaciente, fechacreacion)

        tipolayout = 'layoutinicio2.html'
        return render_template("listaformulariospaciente.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, fechacreacion=fechacreacion, datosformularioantecedentesestable = datosformularioantecedentesestable, datosescalapanasestable = datosescalapanasestable, datosescalafastestable = datosescalafastestable, datosescalawhoqolestable = datosescalawhoqolestable, datosescalaeeagestable = datosescalaeeagestable, datoscuestionarioavataresestable = datoscuestionarioavataresestable, datosappcaraspantallaestable = datosappcaraspantallaestable, datosappcarasvrestable = datosappcarasvrestable, datosescalaminicertsestable = datosescalaminicertsestable, datosescalaius12estable = datosescalaius12estable, datosescalaebrdestable = datosescalaebrdestable, datosescalabdiiiestable = datosescalabdiiiestable, datosescalashortstairestable = datosescalashortstairestable, datosescalahrsdestable = datosescalahrsdestable, datosformularioantecedentesinestable = datosformularioantecedentesinestable, datosescalapanasinestable = datosescalapanasinestable, datosescalafastinestable = datosescalafastinestable, datosescalawhoqolinestable = datosescalawhoqolinestable, datosescalaeeaginestable = datosescalaeeaginestable, datoscuestionarioavataresinestable = datoscuestionarioavataresinestable, datosappcaraspantallainestable = datosappcaraspantallainestable, datosappcarasvrinestable = datosappcarasvrinestable, datosescalaminicertsinestable = datosescalaminicertsinestable, datosescalaius12inestable = datosescalaius12inestable, datosescalaebrdinestable = datosescalaebrdinestable, datosescalabdiiiinestable = datosescalabdiiiinestable, datosescalashortstairinestable = datosescalashortstairinestable, datosescalahrsdinestable = datosescalahrsdinestable) 


    elif tipopaciente == "bipolar":
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


    
    elif tipopaciente == "esquizofrenia":
        # hay que pasar los datos de todas las formularios secundarios y escalas en su version estable e inestable (19 escalas)

        datosformularioantecedentesestable = buscarfirstpaciente(Formularioantecedentesesquizofreniaestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalapanasestable = buscarfirstpaciente(Escalapanasesquizofreniaestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalafastestable = buscarfirstpaciente(Escalafastesquizofreniaestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalawhoqolestable = buscarfirstpaciente(Escalawhoqolesquizofreniaestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalaeeagestable = buscarfirstpaciente(Escalaeeagesquizofreniaestable, idpaciente, nhcpaciente, fechacreacion)
        datoscuestionarioavataresestable = buscarfirstpaciente(Cuestionarioavataresesquizofreniaestable, idpaciente, nhcpaciente, fechacreacion)
        
        datosappcaraspantallaestable = buscarfirstpacienteappcaras(Appcaraspantallaesquizofreniaestable, idpaciente, nhcpaciente)
        datosappcarasvrestable = buscarfirstpacienteappcaras(Appcarasvresquizofreniaestable, idpaciente, nhcpaciente)
        
        datosescalapanssestable = buscarfirstpaciente(Escalapanssesquizofreniaestable, idpaciente, nhcpaciente, fechacreacion)


        datosformularioantecedentesinestable = buscarfirstpaciente(Formularioantecedentesesquizofreniainestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalapanasinestable = buscarfirstpaciente(Escalapanasesquizofreniainestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalafastinestable = buscarfirstpaciente(Escalafastesquizofreniainestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalawhoqolinestable = buscarfirstpaciente(Escalawhoqolesquizofreniainestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalaeeaginestable = buscarfirstpaciente(Escalaeeagesquizofreniainestable, idpaciente, nhcpaciente, fechacreacion)
        datoscuestionarioavataresinestable = buscarfirstpaciente(Cuestionarioavataresesquizofreniainestable, idpaciente, nhcpaciente, fechacreacion)
        
        datosappcaraspantallainestable = buscarfirstpacienteappcaras(Appcaraspantallaesquizofreniainestable, idpaciente, nhcpaciente)
        datosappcarasvrinestable = buscarfirstpacienteappcaras(Appcarasvresquizofreniainestable, idpaciente, nhcpaciente)

        datosescalapanssinestable = buscarfirstpaciente(Escalapanssesquizofreniainestable, idpaciente, nhcpaciente, fechacreacion)

        tipolayout = 'layoutinicio2.html'
        return render_template("listaformulariospaciente.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, fechacreacion=fechacreacion, datosformularioantecedentesestable = datosformularioantecedentesestable, datosescalapanasestable = datosescalapanasestable, datosescalafastestable = datosescalafastestable, datosescalawhoqolestable = datosescalawhoqolestable, datosescalaeeagestable = datosescalaeeagestable, datoscuestionarioavataresestable = datoscuestionarioavataresestable, datosappcaraspantallaestable = datosappcaraspantallaestable, datosappcarasvrestable = datosappcarasvrestable, datosescalapanssestable = datosescalapanssestable, datosformularioantecedentesinestable = datosformularioantecedentesinestable, datosescalapanasinestable = datosescalapanasinestable, datosescalafastinestable = datosescalafastinestable, datosescalawhoqolinestable = datosescalawhoqolinestable, datosescalaeeaginestable = datosescalaeeaginestable, datoscuestionarioavataresinestable = datoscuestionarioavataresinestable, datosappcaraspantallainestable = datosappcaraspantallainestable, datosappcarasvrinestable = datosappcarasvrinestable, datosescalapanssinestable = datosescalapanssinestable)



    elif tipopaciente == "esquizoafectivo":
        # hay que pasar los datos de todas las formularios secundarios y escalas en su version estable e inestable (23 escalas)

        datosformularioantecedentesestable = buscarfirstpaciente(Formularioantecedentesesquizoafectivoestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalapanasestable = buscarfirstpaciente(Escalapanasesquizoafectivoestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalafastestable = buscarfirstpaciente(Escalafastesquizoafectivoestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalawhoqolestable = buscarfirstpaciente(Escalawhoqolesquizoafectivoestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalaeeagestable = buscarfirstpaciente(Escalaeeagesquizoafectivoestable, idpaciente, nhcpaciente, fechacreacion)
        datoscuestionarioavataresestable = buscarfirstpaciente(Cuestionarioavataresesquizoafectivoestable, idpaciente, nhcpaciente, fechacreacion)

        datosappcaraspantallaestable = buscarfirstpacienteappcaras(Appcaraspantallaesquizoafectivoestable, idpaciente, nhcpaciente)
        datosappcarasvrestable = buscarfirstpacienteappcaras(Appcarasvresquizoafectivoestable, idpaciente, nhcpaciente)

        datosescalamadrsestable = buscarfirstpaciente(Escalamadrsesquizoafectivoestable, idpaciente, nhcpaciente, fechacreacion) 
        datosescalaymrsestable = buscarfirstpaciente(Escalaymrsesquizoafectivoestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalapanssestable = buscarfirstpaciente(Escalapanssesquizoafectivoestable, idpaciente, nhcpaciente, fechacreacion)


        datosformularioantecedentesinestable = buscarfirstpaciente(Formularioantecedentesesquizoafectivoinestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalapanasinestable = buscarfirstpaciente(Escalapanasesquizoafectivoinestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalafastinestable = buscarfirstpaciente(Escalafastesquizoafectivoinestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalawhoqolinestable = buscarfirstpaciente(Escalawhoqolesquizoafectivoinestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalaeeaginestable = buscarfirstpaciente(Escalaeeagesquizoafectivoinestable, idpaciente, nhcpaciente, fechacreacion)
        datoscuestionarioavataresinestable = buscarfirstpaciente(Cuestionarioavataresesquizoafectivoinestable, idpaciente, nhcpaciente, fechacreacion)

        datosappcaraspantallainestable = buscarfirstpacienteappcaras(Appcaraspantallaesquizoafectivoinestable, idpaciente, nhcpaciente)
        datosappcarasvrinestable = buscarfirstpacienteappcaras(Appcarasvresquizoafectivoinestable, idpaciente, nhcpaciente)

        datosescalamadrsinestable = buscarfirstpaciente(Escalamadrsesquizoafectivoinestable, idpaciente, nhcpaciente, fechacreacion) 
        datosescalaymrsinestable = buscarfirstpaciente(Escalaymrsesquizoafectivoinestable, idpaciente, nhcpaciente, fechacreacion)
        datosescalapanssinestable = buscarfirstpaciente(Escalapanssesquizoafectivoinestable, idpaciente, nhcpaciente, fechacreacion)

        tipolayout = 'layoutinicio2.html'
        return render_template("listaformulariospaciente.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, fechacreacion=fechacreacion, datosformularioantecedentesestable = datosformularioantecedentesestable, datosescalapanasestable = datosescalapanasestable, datosescalafastestable = datosescalafastestable, datosescalawhoqolestable = datosescalawhoqolestable, datosescalaeeagestable = datosescalaeeagestable, datoscuestionarioavataresestable = datoscuestionarioavataresestable, datosappcaraspantallaestable = datosappcaraspantallaestable, datosappcarasvrestable = datosappcarasvrestable, datosescalamadrsestable = datosescalamadrsestable, datosescalaymrsestable = datosescalaymrsestable, datosescalapanssestable = datosescalapanssestable, datosformularioantecedentesinestable = datosformularioantecedentesinestable, datosescalapanasinestable = datosescalapanasinestable, datosescalafastinestable = datosescalafastinestable, datosescalawhoqolinestable = datosescalawhoqolinestable, datosescalaeeaginestable = datosescalaeeaginestable, datoscuestionarioavataresinestable = datoscuestionarioavataresinestable, datosappcaraspantallainestable = datosappcaraspantallainestable, datosappcarasvrinestable = datosappcarasvrinestable, datosescalamadrsinestable = datosescalamadrsinestable, datosescalaymrsinestable = datosescalaymrsinestable, datosescalapanssinestable = datosescalapanssinestable)




# fin pagina lista formularios del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////









# pagina formulario de registro del paciente ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# para crear y modificar el formulario de registro, y para crear el esquema de los formularios secundarios y escalas 

@appcarasestableinestable.route("/formularioregistro/<string:tipopaciente>/", methods=["GET", "POST"])
@appcarasestableinestable.route("/formularioregistro/<string:tipopaciente>/<int:idpaciente>/", methods=["GET", "POST"])
def mostrarformularioregistro(tipopaciente="", idpaciente=None ):
    if request.method == 'POST':

        if tipopaciente == "depresion":
            nombretablabd = Formularioregistrodepresion
            listaescalas = [Formularioantecedentesdepresionestable, Formularioantecedentesdepresioninestable, Escalaminicertsdepresionestable, Escalaius12depresionestable, Escalaebrddepresionestable, Escalabdiiidepresionestable, Escalashortstairdepresionestable, Escalahrsddepresionestable, Escalapanasdepresionestable, Escalafastdepresionestable, Escalawhoqoldepresionestable, Escalaeeagdepresionestable, Cuestionarioavataresdepresionestable, Escalaminicertsdepresioninestable, Escalaius12depresioninestable, Escalaebrddepresioninestable, Escalabdiiidepresioninestable, Escalashortstairdepresioninestable, Escalahrsddepresioninestable, Escalapanasdepresioninestable, Escalafastdepresioninestable, Escalawhoqoldepresioninestable, Escalaeeagdepresioninestable, Cuestionarioavataresdepresioninestable]
            listaappcaras = [Appcaraspantalladepresionestable, Appcarasvrdepresionestable, Appcaraspantalladepresioninestable, Appcarasvrdepresioninestable]

        elif tipopaciente == "bipolar":
            nombretablabd = Formularioregistrobipolar
            listaescalas = [Formularioantecedentesbipolarestable, Formularioantecedentesbipolarinestable, Escalamadrsbipolarestable, Escalaymrsbipolarestable, Escalapanasbipolarestable, Escalafastbipolarestable, Escalawhoqolbipolarestable, Escalaeeagbipolarestable, Cuestionarioavataresbipolarestable, Escalamadrsbipolarinestable, Escalaymrsbipolarinestable, Escalapanasbipolarinestable, Escalafastbipolarinestable, Escalawhoqolbipolarinestable, Escalaeeagbipolarinestable, Cuestionarioavataresbipolarinestable]
            listaappcaras = [Appcaraspantallabipolarestable, Appcarasvrbipolarestable, Appcaraspantallabipolarinestable, Appcarasvrbipolarinestable]

        elif tipopaciente == "esquizofrenia":
            nombretablabd = Formularioregistroesquizofrenia
            listaescalas = [Formularioantecedentesesquizofreniaestable, Formularioantecedentesesquizofreniainestable, Escalapanssesquizofreniaestable, Escalapanasesquizofreniaestable, Escalafastesquizofreniaestable, Escalawhoqolesquizofreniaestable, Escalaeeagesquizofreniaestable, Cuestionarioavataresesquizofreniaestable, Escalapanssesquizofreniainestable, Escalapanasesquizofreniainestable, Escalafastesquizofreniainestable, Escalawhoqolesquizofreniainestable, Escalaeeagesquizofreniainestable, Cuestionarioavataresesquizofreniainestable]
            listaappcaras = [Appcaraspantallaesquizofreniaestable, Appcarasvresquizofreniaestable, Appcaraspantallaesquizofreniainestable, Appcarasvresquizofreniainestable]

        elif tipopaciente == "esquizoafectivo":
            nombretablabd = Formularioregistroesquizoafectivo
            listaescalas = [Formularioantecedentesesquizoafectivoestable, Formularioantecedentesesquizoafectivoinestable, Escalapanssesquizoafectivoestable, Escalamadrsesquizoafectivoestable, Escalaymrsesquizoafectivoestable, Escalapanasesquizoafectivoestable, Escalafastesquizoafectivoestable, Escalawhoqolesquizoafectivoestable, Escalaeeagesquizoafectivoestable, Cuestionarioavataresesquizoafectivoestable, Escalapanssesquizoafectivoinestable, Escalamadrsesquizoafectivoinestable, Escalaymrsesquizoafectivoinestable, Escalapanasesquizoafectivoinestable, Escalafastesquizoafectivoinestable, Escalawhoqolesquizoafectivoinestable, Escalaeeagesquizoafectivoinestable, Cuestionarioavataresesquizoafectivoinestable]
            listaappcaras = [Appcaraspantallaesquizoafectivoestable, Appcarasvresquizoafectivoestable, Appcaraspantallaesquizoafectivoinestable, Appcarasvresquizoafectivoinestable]

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

    if tipopaciente == "depresion":
        nombretablabd = Formularioregistrodepresion
        tipolayout = 'layoutinicio2.html'
    
    elif tipopaciente == "bipolar":
        nombretablabd = Formularioregistrobipolar
        tipolayout = 'layoutinicio2.html'
    
    elif tipopaciente == "esquizofrenia":
        nombretablabd = Formularioregistroesquizofrenia
        tipolayout = 'layoutinicio2.html'

    elif tipopaciente == "esquizoafectivo":
        nombretablabd = Formularioregistroesquizoafectivo
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



@appcarasestableinestable.route("/formularioantecedentes/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarformularioantecedentes(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            #  hay que ver que la escala pertenezca a al tipo de paciente, sino no es necesaria colocar la condicion
            if tipopaciente == "depresion":
                if estadopaciente =="estable":
                    nombretablabd = Formularioantecedentesdepresionestable
                elif estadopaciente =="inestable":
                    nombretablabd = Formularioantecedentesdepresioninestable
            
            elif tipopaciente == "bipolar":
                if estadopaciente =="estable":
                    nombretablabd = Formularioantecedentesbipolarestable
                elif estadopaciente =="inestable":
                    nombretablabd = Formularioantecedentesbipolarinestable
            
            elif tipopaciente == "esquizofrenia":
                if estadopaciente =="estable":
                    nombretablabd = Formularioantecedentesesquizofreniaestable
                elif estadopaciente =="inestable":
                    nombretablabd = Formularioantecedentesesquizofreniainestable

            elif tipopaciente == "esquizoafectivo":
                if estadopaciente =="estable":
                    nombretablabd = Formularioantecedentesesquizoafectivoestable
                elif estadopaciente =="inestable":
                    nombretablabd = Formularioantecedentesesquizoafectivoinestable
            

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
    if tipopaciente == "depresion":
        if estadopaciente =="estable":
            nombretablabd = Formularioantecedentesdepresionestable
        elif estadopaciente =="inestable":
            nombretablabd = Formularioantecedentesdepresioninestable
        tipolayout = 'layoutescalasdepresion.html'
    
    elif tipopaciente == "bipolar":
        if estadopaciente =="estable":
            nombretablabd = Formularioantecedentesbipolarestable
        elif estadopaciente =="inestable":
            nombretablabd = Formularioantecedentesbipolarinestable
        tipolayout = 'layoutescalasdepresion.html'
    
    elif tipopaciente == "esquizofrenia":
        if estadopaciente =="estable":
            nombretablabd = Formularioantecedentesesquizofreniaestable
        elif estadopaciente =="inestable":
            nombretablabd = Formularioantecedentesesquizofreniainestable
        tipolayout = 'layoutescalasdepresion.html'

    elif tipopaciente == "esquizoafectivo":
        if estadopaciente =="estable":
            nombretablabd = Formularioantecedentesesquizoafectivoestable
        elif estadopaciente =="inestable":
            nombretablabd = Formularioantecedentesesquizoafectivoinestable
        tipolayout = 'layoutescalasdepresion.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("formularioantecedentes.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)














# escala minicerts ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route("/escalaminicerts/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalaminicerts(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            #  hay que ver que la escala pertenezca a al tipo de paciente, sino no es necesaria colocar la condicion
            if tipopaciente == "depresion":
                if estadopaciente =="estable":
                    nombretablabd = Escalaminicertsdepresionestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalaminicertsdepresioninestable
            

            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala
            formularioget.escalaminicerts1 = request.form.get('escalaminicerts1')
            formularioget.escalaminicerts2 = request.form.get('escalaminicerts2')
            formularioget.escalaminicerts3 = request.form.get('escalaminicerts3')
            formularioget.escalaminicerts4 = request.form.get('escalaminicerts4')
            formularioget.escalaminicerts5 = request.form.get('escalaminicerts5')
            formularioget.escalaminicerts6 = request.form.get('escalaminicerts6')
            formularioget.escalaminicerts7 = request.form.get('escalaminicerts7')
            formularioget.escalaminicerts8 = request.form.get('escalaminicerts8')
            formularioget.escalaminicerts9 = request.form.get('escalaminicerts9')
            formularioget.escalaminicerts10 = request.form.get('escalaminicerts10')
            formularioget.escalaminicerts11 = request.form.get('escalaminicerts11')
            formularioget.escalaminicerts12 = request.form.get('escalaminicerts12')
            formularioget.escalaminicerts13 = request.form.get('escalaminicerts13')
            formularioget.escalaminicerts14 = request.form.get('escalaminicerts14')
            formularioget.escalaminicerts15= request.form.get('escalaminicerts15')
            formularioget.escalaminicerts16 = request.form.get('escalaminicerts16')
            
            
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
    if tipopaciente == "depresion":
        if estadopaciente =="estable":
            nombretablabd = Escalaminicertsdepresionestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalaminicertsdepresioninestable
        tipolayout = 'layoutescalasdepresion.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/escalaminicerts.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)




# escala escalaius12 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route("/escalaius12/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalaius12(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            #  hay que ver que la escala pertenezca a al tipo de paciente, sino no es necesaria colocar la condicion
            if tipopaciente == "depresion":
                if estadopaciente =="estable":
                    nombretablabd = Escalaius12depresionestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalaius12depresioninestable
            

            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala
            formularioget.escalaius12_1 = request.form.get('escalaius12_1')
            formularioget.escalaius12_2 = request.form.get('escalaius12_2')
            formularioget.escalaius12_3 = request.form.get('escalaius12_3')
            formularioget.escalaius12_4 = request.form.get('escalaius12_4')
            formularioget.escalaius12_5 = request.form.get('escalaius12_5')
            formularioget.escalaius12_6 = request.form.get('escalaius12_6')
            formularioget.escalaius12_7 = request.form.get('escalaius12_7')
            formularioget.escalaius12_8 = request.form.get('escalaius12_8')
            formularioget.escalaius12_9 = request.form.get('escalaius12_9')
            formularioget.escalaius12_10 = request.form.get('escalaius12_10')
            formularioget.escalaius12_11 = request.form.get('escalaius12_11')
            formularioget.escalaius12_12 = request.form.get('escalaius12_12')
            
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
    if tipopaciente == "depresion":
        if estadopaciente =="estable":
            nombretablabd = Escalaius12depresionestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalaius12depresioninestable
        tipolayout = 'layoutescalasdepresion.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/escalaius12.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)





# escala ebrd ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route("/escalaebrd/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalaebrd(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            #  hay que ver que la escala pertenezca a al tipo de paciente, sino no es necesaria colocar la condicion
            if tipopaciente == "depresion":
                if estadopaciente =="estable":
                    nombretablabd = Escalaebrddepresionestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalaebrddepresioninestable
            

            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala
            formularioget.escalaebrd1 = request.form.get('escalaebrd1')
            formularioget.escalaebrd2 = request.form.get('escalaebrd2')
            formularioget.escalaebrd3 = request.form.get('escalaebrd3')
            formularioget.escalaebrd4 = request.form.get('escalaebrd4')
            
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
    if tipopaciente == "depresion":
        if estadopaciente =="estable":
            nombretablabd = Escalaebrddepresionestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalaebrddepresioninestable
        tipolayout = 'layoutescalasdepresion.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/escalaebrd.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)



# escala bdiii ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route("/escalabdiii/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalabdiii(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            #  hay que ver que la escala pertenezca a al tipo de paciente, sino no es necesaria colocar la condicion
            if tipopaciente == "depresion":
                if estadopaciente =="estable":
                    nombretablabd = Escalabdiiidepresionestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalabdiiidepresioninestable
            

            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala
            formularioget.escalabdiii1 = request.form.get('escalabdiii1')
            formularioget.escalabdiii2 = request.form.get('escalabdiii2')
            formularioget.escalabdiii3 = request.form.get('escalabdiii3')
            formularioget.escalabdiii4 = request.form.get('escalabdiii4')
            formularioget.escalabdiii5 = request.form.get('escalabdiii5')
            formularioget.escalabdiii6 = request.form.get('escalabdiii6')
            formularioget.escalabdiii7 = request.form.get('escalabdiii7')
            formularioget.escalabdiii8 = request.form.get('escalabdiii8')
            formularioget.escalabdiii9 = request.form.get('escalabdiii9')
            formularioget.escalabdiii10 = request.form.get('escalabdiii10')
            formularioget.escalabdiii11 = request.form.get('escalabdiii11')
            formularioget.escalabdiii12 = request.form.get('escalabdiii12')
            formularioget.escalabdiii13 = request.form.get('escalabdiii13')
            formularioget.escalabdiii14 = request.form.get('escalabdiii14')
            formularioget.escalabdiii15 = request.form.get('escalabdiii15')
            formularioget.escalabdiii16 = request.form.get('escalabdiii16')
            formularioget.escalabdiii17 = request.form.get('escalabdiii17')
            formularioget.escalabdiii18 = request.form.get('escalabdiii18')
            formularioget.escalabdiii19 = request.form.get('escalabdiii19')
            formularioget.escalabdiii20 = request.form.get('escalabdiii20')
            formularioget.escalabdiii21 = request.form.get('escalabdiii21')
            
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
    if tipopaciente == "depresion":
        if estadopaciente =="estable":
            nombretablabd = Escalabdiiidepresionestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalabdiiidepresioninestable
        tipolayout = 'layoutescalasdepresion.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/escalabdiii.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)




# escala shortstair ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route("/escalashortstair/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalashortstair(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            #  hay que ver que la escala pertenezca a al tipo de paciente, sino no es necesaria colocar la condicion
            if tipopaciente == "depresion":
                if estadopaciente =="estable":
                    nombretablabd = Escalashortstairdepresionestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalashortstairdepresioninestable
            

            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala
            formularioget.escalashortstair1 = request.form.get('escalashortstair1')
            formularioget.escalashortstair2 = request.form.get('escalashortstair2')
            formularioget.escalashortstair3 = request.form.get('escalashortstair3')
            formularioget.escalashortstair4 = request.form.get('escalashortstair4')
            formularioget.escalashortstair5 = request.form.get('escalashortstair5')
            formularioget.escalashortstair6 = request.form.get('escalashortstair6')
            formularioget.escalashortstair7 = request.form.get('escalashortstair7')
            formularioget.escalashortstair8 = request.form.get('escalashortstair8')
            
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
    if tipopaciente == "depresion":
        if estadopaciente =="estable":
            nombretablabd = Escalashortstairdepresionestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalashortstairdepresioninestable
        tipolayout = 'layoutescalasdepresion.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/escalashortstair.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)






# escala hrsd ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route("/escalahrsd/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalahrsd(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            #  hay que ver que la escala pertenezca a al tipo de paciente, sino no es necesaria colocar la condicion
            if tipopaciente == "depresion":
                if estadopaciente =="estable":
                    nombretablabd = Escalahrsddepresionestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalahrsddepresioninestable
            

            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala
            formularioget.escalahrsd1 = request.form.get('escalahrsd1')
            formularioget.escalahrsd2 = request.form.get('escalahrsd2')
            formularioget.escalahrsd3 = request.form.get('escalahrsd3')
            formularioget.escalahrsd4 = request.form.get('escalahrsd4')
            formularioget.escalahrsd5 = request.form.get('escalahrsd5')
            formularioget.escalahrsd6 = request.form.get('escalahrsd6')
            formularioget.escalahrsd7 = request.form.get('escalahrsd7')
            formularioget.escalahrsd8 = request.form.get('escalahrsd8')
            formularioget.escalahrsd9 = request.form.get('escalahrsd9')
            formularioget.escalahrsd10 = request.form.get('escalahrsd10')
            formularioget.escalahrsd11 = request.form.get('escalahrsd11')
            formularioget.escalahrsd12 = request.form.get('escalahrsd12')
            formularioget.escalahrsd13 = request.form.get('escalahrsd13')
            formularioget.escalahrsd14 = request.form.get('escalahrsd14')
            formularioget.escalahrsd15= request.form.get('escalahrsd15')
            formularioget.escalahrsd16 = request.form.get('escalahrsd16')
            formularioget.escalahrsd17 = request.form.get('escalahrsd17')
            
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
    if tipopaciente == "depresion":
        if estadopaciente =="estable":
            nombretablabd = Escalahrsddepresionestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalahrsddepresioninestable
        tipolayout = 'layoutescalasdepresion.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/escalahrsd.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)






# escala madrs ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route("/escalamadrs/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalamadrs(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            if tipopaciente == "bipolar":
                if estadopaciente =="estable":
                    nombretablabd = Escalamadrsbipolarestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalamadrsbipolarinestable

            
            elif tipopaciente == "esquizoafectivo":
                if estadopaciente =="estable":
                    nombretablabd = Escalamadrsesquizoafectivoestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalamadrsesquizoafectivoinestable


            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala
            formularioget.escalamadrs1 = request.form.get('escalamadrs1')
            formularioget.escalamadrs2 = request.form.get('escalamadrs2')
            formularioget.escalamadrs3 = request.form.get('escalamadrs3')
            formularioget.escalamadrs4 = request.form.get('escalamadrs4')
            formularioget.escalamadrs5 = request.form.get('escalamadrs5')
            formularioget.escalamadrs6 = request.form.get('escalamadrs6')
            formularioget.escalamadrs7 = request.form.get('escalamadrs7')
            formularioget.escalamadrs8 = request.form.get('escalamadrs8')
            formularioget.escalamadrs9 = request.form.get('escalamadrs9')
            formularioget.escalamadrs10 = request.form.get('escalamadrs10')
            
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
            nombretablabd = Escalamadrsbipolarestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalamadrsbipolarinestable
        tipolayout = 'layoutescalasbipolar.html'
    
    elif tipopaciente == "esquizoafectivo":
        if estadopaciente =="estable":
            nombretablabd = Escalamadrsesquizoafectivoestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalamadrsesquizoafectivoinestable
        tipolayout = 'layoutescalasesquizoafectivo.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/escalamadrs.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)





# escala ymrs ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route("/escalaymrs/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalaymrs(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            if tipopaciente == "bipolar":
                if estadopaciente =="estable":
                    nombretablabd = Escalaymrsbipolarestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalaymrsbipolarinestable

            
            elif tipopaciente == "esquizoafectivo":
                if estadopaciente =="estable":
                    nombretablabd = Escalaymrsesquizoafectivoestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalaymrsesquizoafectivoinestable


            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala
            formularioget.escalaymrs1 = request.form.get('escalaymrs1')
            formularioget.escalaymrs2 = request.form.get('escalaymrs2')
            formularioget.escalaymrs3 = request.form.get('escalaymrs3')
            formularioget.escalaymrs4 = request.form.get('escalaymrs4')
            formularioget.escalaymrs5 = request.form.get('escalaymrs5')
            formularioget.escalaymrs6 = request.form.get('escalaymrs6')
            formularioget.escalaymrs7 = request.form.get('escalaymrs7')
            formularioget.escalaymrs8 = request.form.get('escalaymrs8')
            formularioget.escalaymrs9 = request.form.get('escalaymrs9')
            formularioget.escalaymrs10 = request.form.get('escalaymrs10')
            formularioget.escalaymrs11 = request.form.get('escalaymrs11')

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
            nombretablabd = Escalaymrsbipolarestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalaymrsbipolarinestable
        tipolayout = 'layoutescalasbipolar.html'
    
    elif tipopaciente == "esquizoafectivo":
        if estadopaciente =="estable":
            nombretablabd = Escalaymrsesquizoafectivoestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalaymrsesquizoafectivoinestable
        tipolayout = 'layoutescalasesquizoafectivo.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/escalaymrs.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)





# escala panss ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route("/escalapanss/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalapanss(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            if tipopaciente == "esquizofrenia":
                if estadopaciente =="estable":
                    nombretablabd = Escalapanssesquizofreniaestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalapanssesquizofreniainestable

            
            elif tipopaciente == "esquizoafectivo":
                if estadopaciente =="estable":
                    nombretablabd = Escalapanssesquizoafectivoestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalapanssesquizoafectivoinestable


            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala
            formularioget.escalapanss1 = request.form.get('escalapanss1')
            formularioget.escalapanss2 = request.form.get('escalapanss2')
            formularioget.escalapanss3 = request.form.get('escalapanss3')
            formularioget.escalapanss4 = request.form.get('escalapanss4')
            formularioget.escalapanss5 = request.form.get('escalapanss5')
            formularioget.escalapanss6 = request.form.get('escalapanss6')
            formularioget.escalapanss7 = request.form.get('escalapanss7')
            formularioget.escalapanss8 = request.form.get('escalapanss8')
            formularioget.escalapanss9 = request.form.get('escalapanss9')
            formularioget.escalapanss10 = request.form.get('escalapanss10')
            formularioget.escalapanss11 = request.form.get('escalapanss11')
            formularioget.escalapanss12 = request.form.get('escalapanss12')
            formularioget.escalapanss13 = request.form.get('escalapanss13')
            formularioget.escalapanss14 = request.form.get('escalapanss14')
            formularioget.escalapanss15 = request.form.get('escalapanss15')
            formularioget.escalapanss16 = request.form.get('escalapanss16')
            formularioget.escalapanss17 = request.form.get('escalapanss17')
            formularioget.escalapanss18 = request.form.get('escalapanss18')
            formularioget.escalapanss19 = request.form.get('escalapanss19')
            formularioget.escalapanss20 = request.form.get('escalapanss20')
            formularioget.escalapanss21 = request.form.get('escalapanss21')
            formularioget.escalapanss22 = request.form.get('escalapanss22')
            formularioget.escalapanss23 = request.form.get('escalapanss23')
            formularioget.escalapanss24 = request.form.get('escalapanss24')
            formularioget.escalapanss25 = request.form.get('escalapanss25')
            formularioget.escalapanss26 = request.form.get('escalapanss26')
            formularioget.escalapanss27 = request.form.get('escalapanss27')
            formularioget.escalapanss28 = request.form.get('escalapanss28')
            formularioget.escalapanss29 = request.form.get('escalapanss29')
            formularioget.escalapanss30 = request.form.get('escalapanss30')

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

    if tipopaciente == "esquizofrenia":
        if estadopaciente =="estable":
            nombretablabd = Escalapanssesquizofreniaestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalapanssesquizofreniainestable
        tipolayout = 'layoutescalasesquizofrenia.html'
    
    elif tipopaciente == "esquizoafectivo":
        if estadopaciente =="estable":
            nombretablabd = Escalapanssesquizoafectivoestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalapanssesquizoafectivoinestable
        tipolayout = 'layoutescalasesquizoafectivo.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/escalapanss.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)





# escala panas ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route("/escalapanas/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalapanas(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            if tipopaciente == "depresion":
                if estadopaciente =="estable":
                    nombretablabd = Escalapanasdepresionestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalapanasdepresioninestable
            
            elif tipopaciente == "bipolar":
                if estadopaciente =="estable":
                    nombretablabd = Escalapanasbipolarestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalapanasbipolarinestable

            elif tipopaciente == "esquizofrenia":
                if estadopaciente =="estable":
                    nombretablabd = Escalapanasesquizofreniaestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalapanasesquizofreniainestable

            elif tipopaciente == "esquizoafectivo":
                if estadopaciente =="estable":
                    nombretablabd = Escalapanasesquizoafectivoestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalapanasesquizoafectivoinestable


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

    if tipopaciente == "depresion":
        if estadopaciente =="estable":
            nombretablabd = Escalapanasdepresionestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalapanasdepresioninestable
        tipolayout = 'layoutescalasdepresion.html'
    
    elif tipopaciente == "bipolar":
        if estadopaciente =="estable":
            nombretablabd = Escalapanasbipolarestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalapanasbipolarinestable
        tipolayout = 'layoutescalasbipolar.html'

    elif tipopaciente == "esquizofrenia":
        if estadopaciente =="estable":
            nombretablabd = Escalapanasesquizofreniaestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalapanasesquizofreniainestable
        tipolayout = 'layoutescalasesquizofrenia.html'

    elif tipopaciente == "esquizoafectivo":
        if estadopaciente =="estable":
            nombretablabd = Escalapanasesquizoafectivoestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalapanasesquizoafectivoinestable
        tipolayout = 'layoutescalasesquizoafectivo.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/escalapanas.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)




# escala fast ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route("/escalafast/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalafast(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            if tipopaciente == "depresion":
                if estadopaciente =="estable":
                    nombretablabd = Escalafastdepresionestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalafastdepresioninestable
            
            elif tipopaciente == "bipolar":
                if estadopaciente =="estable":
                    nombretablabd = Escalafastbipolarestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalafastbipolarinestable

            elif tipopaciente == "esquizofrenia":
                if estadopaciente =="estable":
                    nombretablabd = Escalafastesquizofreniaestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalafastesquizofreniainestable

            elif tipopaciente == "esquizoafectivo":
                if estadopaciente =="estable":
                    nombretablabd = Escalafastesquizoafectivoestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalafastesquizoafectivoinestable


            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala
            formularioget.escalafast1 = request.form.get('escalafast1')
            formularioget.escalafast2 = request.form.get('escalafast2')
            formularioget.escalafast3 = request.form.get('escalafast3')
            formularioget.escalafast4 = request.form.get('escalafast4')
            formularioget.escalafast5 = request.form.get('escalafast5')
            formularioget.escalafast6 = request.form.get('escalafast6')
            formularioget.escalafast7 = request.form.get('escalafast7')
            formularioget.escalafast8 = request.form.get('escalafast8')
            formularioget.escalafast9 = request.form.get('escalafast9')
            formularioget.escalafast10 = request.form.get('escalafast10')
            formularioget.escalafast11 = request.form.get('escalafast11')
            formularioget.escalafast12 = request.form.get('escalafast12')
            formularioget.escalafast13 = request.form.get('escalafast13')
            formularioget.escalafast14 = request.form.get('escalafast14')
            formularioget.escalafast15 = request.form.get('escalafast15')
            formularioget.escalafast16 = request.form.get('escalafast16')
            formularioget.escalafast17 = request.form.get('escalafast17')
            formularioget.escalafast18 = request.form.get('escalafast18')
            formularioget.escalafast19 = request.form.get('escalafast19')
            formularioget.escalafast20 = request.form.get('escalafast20')
            formularioget.escalafast21 = request.form.get('escalafast21')
            formularioget.escalafast22 = request.form.get('escalafast22')
            formularioget.escalafast23 = request.form.get('escalafast23')
            formularioget.escalafast24 = request.form.get('escalafast24')

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

    if tipopaciente == "depresion":
        if estadopaciente =="estable":
            nombretablabd = Escalafastdepresionestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalafastdepresioninestable
        tipolayout = 'layoutescalasdepresion.html'
    
    elif tipopaciente == "bipolar":
        if estadopaciente =="estable":
            nombretablabd = Escalafastbipolarestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalafastbipolarinestable
        tipolayout = 'layoutescalasbipolar.html'

    elif tipopaciente == "esquizofrenia":
        if estadopaciente =="estable":
            nombretablabd = Escalafastesquizofreniaestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalafastesquizofreniainestable
        tipolayout = 'layoutescalasesquizofrenia.html'

    elif tipopaciente == "esquizoafectivo":
        if estadopaciente =="estable":
            nombretablabd = Escalafastesquizoafectivoestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalafastesquizoafectivoinestable
        tipolayout = 'layoutescalasesquizoafectivo.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/escalafast.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)





# escala whoqol ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route("/escalawhoqol/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalawhoqol(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            if tipopaciente == "depresion":
                if estadopaciente =="estable":
                    nombretablabd = Escalawhoqoldepresionestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalawhoqoldepresioninestable
            
            elif tipopaciente == "bipolar":
                if estadopaciente =="estable":
                    nombretablabd = Escalawhoqolbipolarestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalawhoqolbipolarinestable

            elif tipopaciente == "esquizofrenia":
                if estadopaciente =="estable":
                    nombretablabd = Escalawhoqolesquizofreniaestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalawhoqolesquizofreniainestable

            elif tipopaciente == "esquizoafectivo":
                if estadopaciente =="estable":
                    nombretablabd = Escalawhoqolesquizoafectivoestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalawhoqolesquizoafectivoinestable


            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala
            formularioget.escalawhoqol1 = request.form.get('escalawhoqol1')
            formularioget.escalawhoqol2 = request.form.get('escalawhoqol2')
            formularioget.escalawhoqol3 = request.form.get('escalawhoqol3')
            formularioget.escalawhoqol4 = request.form.get('escalawhoqol4')
            formularioget.escalawhoqol5 = request.form.get('escalawhoqol5')
            formularioget.escalawhoqol6 = request.form.get('escalawhoqol6')
            formularioget.escalawhoqol7 = request.form.get('escalawhoqol7')
            formularioget.escalawhoqol8 = request.form.get('escalawhoqol8')
            formularioget.escalawhoqol9 = request.form.get('escalawhoqol9')
            formularioget.escalawhoqol10 = request.form.get('escalawhoqol10')
            formularioget.escalawhoqol11 = request.form.get('escalawhoqol11')
            formularioget.escalawhoqol12 = request.form.get('escalawhoqol12')
            formularioget.escalawhoqol13 = request.form.get('escalawhoqol13')
            formularioget.escalawhoqol14 = request.form.get('escalawhoqol14')
            formularioget.escalawhoqol15 = request.form.get('escalawhoqol15')
            formularioget.escalawhoqol16 = request.form.get('escalawhoqol16')
            formularioget.escalawhoqol17 = request.form.get('escalawhoqol17')
            formularioget.escalawhoqol18 = request.form.get('escalawhoqol18')
            formularioget.escalawhoqol19 = request.form.get('escalawhoqol19')
            formularioget.escalawhoqol20 = request.form.get('escalawhoqol20')
            formularioget.escalawhoqol21 = request.form.get('escalawhoqol21')
            formularioget.escalawhoqol22 = request.form.get('escalawhoqol22')
            formularioget.escalawhoqol23 = request.form.get('escalawhoqol23')
            formularioget.escalawhoqol24 = request.form.get('escalawhoqol24')
            formularioget.escalawhoqol25 = request.form.get('escalawhoqol25')
            formularioget.escalawhoqol26 = request.form.get('escalawhoqol26')
            formularioget.escalawhoqol27 = request.form.get('escalawhoqol27')
            formularioget.escalawhoqol28 = request.form.get('escalawhoqol28')
            formularioget.escalawhoqol29 = request.form.get('escalawhoqol29')

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

    if tipopaciente == "depresion":
        if estadopaciente =="estable":
            nombretablabd = Escalawhoqoldepresionestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalawhoqoldepresioninestable
        tipolayout = 'layoutescalasdepresion.html'
    
    elif tipopaciente == "bipolar":
        if estadopaciente =="estable":
            nombretablabd = Escalawhoqolbipolarestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalawhoqolbipolarinestable
        tipolayout = 'layoutescalasbipolar.html'

    elif tipopaciente == "esquizofrenia":
        if estadopaciente =="estable":
            nombretablabd = Escalawhoqolesquizofreniaestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalawhoqolesquizofreniainestable
        tipolayout = 'layoutescalasesquizofrenia.html'

    elif tipopaciente == "esquizoafectivo":
        if estadopaciente =="estable":
            nombretablabd = Escalawhoqolesquizoafectivoestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalawhoqolesquizoafectivoinestable
        tipolayout = 'layoutescalasesquizoafectivo.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/escalawhoqol.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)






# escala eeag ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route("/escalaeeag/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarescalaeeag(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):

            if tipopaciente == "depresion":
                if estadopaciente =="estable":
                    nombretablabd = Escalaeeagdepresionestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalaeeagdepresioninestable
                tipolayout = 'layoutescalasdepresion.html'
            
            elif tipopaciente == "bipolar":
                if estadopaciente =="estable":
                    nombretablabd = Escalaeeagbipolarestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalaeeagbipolarinestable
                tipolayout = 'layoutescalasbipolar.html'

            elif tipopaciente == "esquizofrenia":
                if estadopaciente =="estable":
                    nombretablabd = Escalaeeagesquizofreniaestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalaeeagesquizofreniainestable
                tipolayout = 'layoutescalasesquizofrenia.html'

            elif tipopaciente == "esquizoafectivo":
                if estadopaciente =="estable":
                    nombretablabd = Escalaeeagesquizoafectivoestable
                elif estadopaciente =="inestable":
                    nombretablabd = Escalaeeagesquizoafectivoinestable
                tipolayout = 'layoutescalasesquizoafectivo.html'

            formularioget = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # colocar los parametros correspondientes para cada escala
            formularioget.escalaeeag1 = request.form.get('escalaeeag1')


            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            formularioget.fechaultimamodificacion = datetime.datetime.today().strftime('%d-%m-%Y %H:%M:%S')
            formularioget.estadoescala = "En Proceso o Finalizada"

            # validacion escala eeag
            eeagcomprobacion = request.form.get('escalaeeag1')
            lista100 = list(range(101))

            if not (eeagcomprobacion in str(lista100)) or (eeagcomprobacion == ""):
                formularioget.estadoescala = "Sin rellenar"

                flash ("Introduce un número valido en el rango  de 0 de 100", category="borrar")
                formulariosecundario = formularioget
                return render_template("/escalaeeag.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)

            else:
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

    if tipopaciente == "depresion":
        if estadopaciente =="estable":
            nombretablabd = Escalaeeagdepresionestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalaeeagdepresioninestable
        tipolayout = 'layoutescalasdepresion.html'
    
    elif tipopaciente == "bipolar":
        if estadopaciente =="estable":
            nombretablabd = Escalaeeagbipolarestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalaeeagbipolarinestable
        tipolayout = 'layoutescalasbipolar.html'

    elif tipopaciente == "esquizofrenia":
        if estadopaciente =="estable":
            nombretablabd = Escalaeeagesquizofreniaestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalaeeagesquizofreniainestable
        tipolayout = 'layoutescalasesquizofrenia.html'

    elif tipopaciente == "esquizoafectivo":
        if estadopaciente =="estable":
            nombretablabd = Escalaeeagesquizoafectivoestable
        elif estadopaciente =="inestable":
            nombretablabd = Escalaeeagesquizoafectivoinestable
        tipolayout = 'layoutescalasesquizoafectivo.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/escalaeeag.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)







# cuestionario avatares ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route("/cuestionarioavatares/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/", methods=["GET", "POST"])
def mostrarcuestionarioavatares(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':
        
        if (request.form.get('botonescalaguardar') == "Guardar") or (request.form.get('botonescalaguardar') == "Guardar Cambios"):
            
            if tipopaciente == "depresion":
                if estadopaciente =="estable":
                    nombretablabd = Cuestionarioavataresdepresionestable
                elif estadopaciente =="inestable":
                    nombretablabd = Cuestionarioavataresdepresioninestable
            
            elif tipopaciente == "bipolar":
                if estadopaciente =="estable":
                    nombretablabd = Cuestionarioavataresbipolarestable
                elif estadopaciente =="inestable":
                    nombretablabd = Cuestionarioavataresbipolarinestable

            elif tipopaciente == "esquizofrenia":
                if estadopaciente =="estable":
                    nombretablabd = Cuestionarioavataresesquizofreniaestable
                elif estadopaciente =="inestable":
                    nombretablabd = Cuestionarioavataresesquizofreniainestable

            elif tipopaciente == "esquizoafectivo":
                if estadopaciente =="estable":
                    nombretablabd = Cuestionarioavataresesquizoafectivoestable
                elif estadopaciente =="inestable":
                    nombretablabd = Cuestionarioavataresesquizoafectivoinestable


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

    if tipopaciente == "depresion":
        if estadopaciente =="estable":
            nombretablabd = Cuestionarioavataresdepresionestable
        elif estadopaciente =="inestable":
            nombretablabd = Cuestionarioavataresdepresioninestable
        tipolayout = 'layoutescalasdepresion.html'
    
    elif tipopaciente == "bipolar":
        if estadopaciente =="estable":
            nombretablabd = Cuestionarioavataresbipolarestable
        elif estadopaciente =="inestable":
            nombretablabd = Cuestionarioavataresbipolarinestable
        tipolayout = 'layoutescalasbipolar.html'

    elif tipopaciente == "esquizofrenia":
        if estadopaciente =="estable":
            nombretablabd = Cuestionarioavataresesquizofreniaestable
        elif estadopaciente =="inestable":
            nombretablabd = Cuestionarioavataresesquizofreniainestable
        tipolayout = 'layoutescalasesquizofrenia.html'

    elif tipopaciente == "esquizoafectivo":
        if estadopaciente =="estable":
            nombretablabd = Cuestionarioavataresesquizoafectivoestable
        elif estadopaciente =="inestable":
            nombretablabd = Cuestionarioavataresesquizoafectivoinestable
        tipolayout = 'layoutescalasesquizoafectivo.html'


    formulariosecundario = buscarfirstpaciente(nombretablabd, idpaciente, nhcpaciente, fechacreacion)
    
    # verifica si existe la tabla y si no existe la crea
    if not formulariosecundario:
        formulariosecundario = crearpacienteescala(nombretablabd, idpaciente, nhcpaciente, fechacreacion)

    return render_template("/cuestionarioavatares.html", tipolayout=tipolayout, tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, formulariosecundario=formulariosecundario)




# fin formularios secundarios y escalas del paciente ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////









#  Appcaraspantalla del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route('/appcaraspantalla/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=['GET','POST'])
def appcaraspantalla(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    
    if tipopaciente == "depresion":
        rutabasedatos = "dbcarasdatosdepresion.db"
        
        if estadopaciente == "estable":
            tipopacienteapp = "Paciente_Depresion_Estable"
            nombretabla = "appcaraspantalladepresionestable"
        elif estadopaciente == "inestable":
            tipopacienteapp = "Paciente_Depresion_Inestable"
            nombretabla = "appcaraspantalladepresioninestable"
    

    elif tipopaciente == "bipolar":
        rutabasedatos = "dbcarasdatosbipolar.db"
        
        if estadopaciente == "estable":
            tipopacienteapp = "Paciente_Bipolar_Estable"
            nombretabla = "appcaraspantallabipolarestable"
        elif estadopaciente == "inestable":
            tipopacienteapp = "Paciente_Bipolar_Inestable"
            nombretabla = "appcaraspantallabipolarinestable"


    elif tipopaciente == "esquizofrenia":
        rutabasedatos = "dbcarasdatosesquizofrenia.db"
        
        if estadopaciente == "estable":
            tipopacienteapp = "Paciente_Esquizofrenia_Estable"
            nombretabla = "appcaraspantallaesquizofreniaestable"
        elif estadopaciente == "inestable":
            tipopacienteapp = "Paciente_Esquizofrenia_Inestable"
            nombretabla = "appcaraspantallaesquizofreniainestable"


    elif tipopaciente == "esquizoafectivo":
        rutabasedatos = "dbcarasdatosesquizoafectivo.db"
        
        if estadopaciente == "estable":
            tipopacienteapp = "Paciente_Esquizoafectivo_Estable"
            nombretabla = "appcaraspantallaesquizoafectivoestable"
        elif estadopaciente == "inestable":
            tipopacienteapp = "Paciente_Esquizoafectivo_Inestable"
            nombretabla = "appcaraspantallaesquizoafectivoinestable"


    # Abre la aplicacion de las caras y le envia la informacion necesaria a los pacientes
    Popen("start carasPantalla.exe "+ str(nhcpaciente) + " " + str(idpaciente) + " " + str(tipopacienteapp) + " " + str(rutabasedatos) + " " + str(nombretabla) , shell= True)

    return render_template('layoutappcaras.html',  tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, fechacreacion=fechacreacion)







#  fin Appcaraspantalla del paciente ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////






#  Resultados Appcaraspantalla del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route('/resultadospacienteappcaraspantalla/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=['GET','POST'])
def resultadospacienteappcaraspantalla(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':

        if request.form.get('resultadosvolver') == "Volver al Paciente":
            return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))

    if tipopaciente == "depresion":
        tipolayout = "layoutresultadosdepresion.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcaraspantalladepresionestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcaraspantalladepresioninestable
    

    elif tipopaciente == "bipolar":
        tipolayout = "layoutresultadosbipolar.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcaraspantallabipolarestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcaraspantallabipolarinestable


    elif tipopaciente == "esquizofrenia":
        tipolayout = "layoutresultadosesquizofrenia.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcaraspantallaesquizofreniaestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcaraspantallaesquizofreniainestable


    elif tipopaciente == "esquizoafectivo":
        tipolayout = "layoutresultadosesquizoafectivo.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcaraspantallaesquizoafectivoestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcaraspantallaesquizoafectivoinestable

    # buscar aciertos por emocion
    aciertosneutral = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "0")
    countaciertosneutral = len(aciertosneutral)
    porcentajeneutral = (countaciertosneutral * 100 )/ 4

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


@appcarasestableinestable.route('/descargarresultadospacienteappcaraspantalla/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=['GET','POST'])
def descargarresultadospacienteappcaraspantalla(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):

    if tipopaciente == "depresion":
        tipolayout = "layoutresultadosdepresion.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcaraspantalladepresionestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcaraspantalladepresioninestable
    
    elif tipopaciente == "bipolar":
        tipolayout = "layoutresultadosbipolar.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcaraspantallabipolarestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcaraspantallabipolarinestable

    elif tipopaciente == "esquizofrenia":
        tipolayout = "layoutresultadosesquizofrenia.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcaraspantallaesquizofreniaestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcaraspantallaesquizofreniainestable

    elif tipopaciente == "esquizoafectivo":
        tipolayout = "layoutresultadosesquizoafectivo.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcaraspantallaesquizoafectivoestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcaraspantallaesquizoafectivoinestable

    # buscar aciertos por emocion
    aciertosneutral = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "0")
    countaciertosneutral = len(aciertosneutral)
    porcentajeneutral = (countaciertosneutral * 100 )/ 4

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

    if len(nhcpaciente) == 1:
        nhcmodificado = nhcpaciente
        if estadopaciente == "estable":
            codigoaplicacion = "RFNIEXXXXX"
        elif estadopaciente == "inestable":
            codigoaplicacion = "RFNIIXXXXX"
        codigocreado = codigoaplicacion + nhcmodificado
        codigo = codigocreado
    
    elif len(nhcpaciente) == 2:
        nhcmodificado = nhcpaciente
        if estadopaciente == "estable":
            codigoaplicacion = "RFNIEXXXX"
        elif estadopaciente == "inestable":
            codigoaplicacion = "RFNIIXXXX"
        codigocreado = codigoaplicacion + nhcmodificado
        codigo = codigocreado

    elif len(nhcpaciente) == 3:
        nhcmodificado = nhcpaciente
        if estadopaciente == "estable":
            codigoaplicacion = "RFNIEXXX"
        elif estadopaciente == "inestable":
            codigoaplicacion = "RFNIIXXX"
        codigocreado = codigoaplicacion + nhcmodificado
        codigo = codigocreado

    elif len(nhcpaciente) == 4:
        nhcmodificado = nhcpaciente
        if estadopaciente == "estable":
            codigoaplicacion = "RFNIEXX"
        elif estadopaciente == "inestable":
            codigoaplicacion = "RFNIIXX"
        codigocreado = codigoaplicacion + nhcmodificado
        codigo = codigocreado

    elif len(nhcpaciente) >= 4:
        nhcmodificado = nhcpaciente[-4:]
        if estadopaciente == "estable":
            codigoaplicacion = "RFNIEXX"
        elif estadopaciente == "inestable":
            codigoaplicacion = "RFNIIXX"
        codigocreado = codigoaplicacion + nhcmodificado
        codigo = codigocreado

    fecha = datetime.datetime.today().strftime('%d-%m-%Y')
    hora = datetime.datetime.today().strftime('%H-%M-%S')

    # generar el pdf, ya sea que se descarge en la carpeta de descargas o para guardar en el escritorio

    # datos del gráfico

    emociones = ['Neutral', 'Sorpresa', 'Miedo', 'Ira', 'Asco', 'Alegría', 'Tristeza']
    porcentajes = [porcentajeneutral, porcentajesorpresa, porcentajemiedo, porcentajeira, porcentajeasco, porcentajealegria, porcentajetristeza]
    posicion = [0, 1, 2, 3, 4, 5, 6]

    #plt.bar(emociones, porcentajes, color='royalblue', alpha=0.7)
    plt.bar(emociones, porcentajes, color=["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#cd3e95", "#cd763e"], alpha=0.7)
    #plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plt.yticks([0, 12.5, 25, 37.5, 50, 62.5, 75, 87.5, 100])
    plt.xlabel('Emociones')
    plt.ylabel('Porcentaje (%)')
    plt.title('Porcentaje de aciertos en cada una de las emociones')

    # Creacion de labels para ponerlos encima de las barras los porcentajes
    label = [str(porcentajeneutral) + '%', str(porcentajesorpresa) + '%', str(porcentajemiedo) +'%', str(porcentajeira) +'%', str(porcentajeasco) +'%', str(porcentajealegria) +'%', str(porcentajetristeza) +'%']
    
    # Poner el texto encima de cada barra
    for i in range(len(emociones)):
        plt.text(x = posicion[i]-0.25 , y = porcentajes[i]+1, s = label[i], size = 8)

    # Ajustar marjenes de la grafica
    #plt.subplots_adjust(bottom= 0.2, top = 0.98)
    
    # guardar la imagen
    plt.savefig('pdf/grafico.png')
    #plt.savefig(f'pdf/{ codigo }.png')
    plt.clf()

    
    # creacion del pdf
    #c = canvas.Canvas("pdf/grafico.pdf", pagesize=A4)
    c = canvas.Canvas(f"pdf/{ codigo }.pdf", pagesize=A4)

    grafico = ImageReader('pdf/grafico.png')
    #grafico = ImageReader(f'pdf/{ codigo }.png')
    #c.drawImage(grafico,   0*mm,   0*mm, width=190*mm,   preserveAspectRatio=True)
    c.drawImage(grafico,   30*mm,   130*mm, width=160*mm,   preserveAspectRatio=True)

    c.setFont('Helvetica', 12)

    c.drawString(50, 410, "En el programa de 'Reconocimiento Facial de Emociones en Realidad Virtual No Inmersiva',")
    c.drawString(50, 395, f"el participante con código: { codigo }, ha conseguido los porcentajes de aciertos para ")
    c.drawString(50, 380, f"cada una de las emociones arriba indicadas.")
        
    c.setFont('Helvetica', 8)
    c.drawString(50, 50, f"Documento generado con fecha { fecha } a las { hora }.")

    c.save()


    # copiar el archivo en escritorio con fecha y hora

    #rutadesktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    rutadesktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
    rutadesktoparchivo = os.path.join(rutadesktop, f'{ codigo }.pdf')


    #shutil.copy(f'pdf/{ codigo }.pdf', os.path.join(rutadesktop, f'{ codigo }_Fecha_'+ fecha + '_Hora_'+ hora +'.pdf'))
    shutil.copy(f'pdf/{ codigo }.pdf', os.path.join(rutadesktop, codigo + '_Fecha_'+ fecha + '_Hora_'+ hora +'.pdf'))

    flash(f"Se ha guardado el archivo '{ codigo }_Fecha_{ fecha }_Hora_{ hora }.pdf' en la carpeta 'Descargas' con los resultados de la 'Aplicación de Reconocimiento Facial en Realidad Virtual No Inmersiva', para el paciente con NHC: { nhcpaciente } en estado { estadopaciente }.", category="crear")


    #eliminar el pdf de la carpeta image para que no se sature con archivos innecesarios
    os.remove(f'pdf/{ codigo }.pdf')


    return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))



#  fin descargar Resultados Appcaraspantalla del paciente ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



































#  Appcarasvr del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




@appcarasestableinestable.route('/appcarasvr/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=['GET','POST'])
def appcarasvr(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    
    if tipopaciente == "depresion":
        rutabasedatos = "dbcarasdatosdepresion.db"
        
        if estadopaciente == "estable":
            tipopacienteapp = "Paciente_Depresion_Estable"
            nombretabla = "appcarasvradepresionestable"
        elif estadopaciente == "inestable":
            tipopacienteapp = "Paciente_Depresion_Inestable"
            nombretabla = "appcarasvrdepresioninestable"
    

    elif tipopaciente == "bipolar":
        rutabasedatos = "dbcarasdatosbipolar.db"
        
        if estadopaciente == "estable":
            tipopacienteapp = "Paciente_Bipolar_Estable"
            nombretabla = "appcarasvrbipolarestable"
        elif estadopaciente == "inestable":
            tipopacienteapp = "Paciente_Bipolar_Inestable"
            nombretabla = "appcarasvrbipolarinestable"


    elif tipopaciente == "esquizofrenia":
        rutabasedatos = "dbcarasdatosesquizofrenia.db"
        
        if estadopaciente == "estable":
            tipopacienteapp = "Paciente_Esquizofrenia_Estable"
            nombretabla = "appcarasvresquizofreniaestable"
        elif estadopaciente == "inestable":
            tipopacienteapp = "Paciente_Esquizofrenia_Inestable"
            nombretabla = "appcarasvresquizofreniainestable"


    elif tipopaciente == "esquizoafectivo":
        rutabasedatos = "dbcarasdatosesquizoafectivo.db"
        
        if estadopaciente == "estable":
            tipopacienteapp = "Paciente_Esquizoafectivo_Estable"
            nombretabla = "appcarasvresquizoafectivoestable"
        elif estadopaciente == "inestable":
            tipopacienteapp = "Paciente_Esquizoafectivo_Inestable"
            nombretabla = "appcarasvresquizoafectivoinestable"


    # Abre la aplicacion de las caras y le envia la informacion necesaria a los pacientes
    Popen("start carasVR.exe "+ str(nhcpaciente) + " " + str(idpaciente) + " " + str(tipopacienteapp) + " " + str(rutabasedatos) + " " + str(nombretabla) , shell= True)
    
    return render_template('layoutappcaras.html',  tipopaciente=tipopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, fechacreacion=fechacreacion)





#  fin Appcarasvr del paciente ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////












#  Resultados Appcarasvr del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route('/resultadospacienteappcarasvr/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=['GET','POST'])
def resultadospacienteappcarasvr(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    if request.method == 'POST':

        if request.form.get('resultadosvolver') == "Volver al Paciente":
            return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))

    if tipopaciente == "depresion":
        tipolayout = "layoutresultadosdepresion.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcarasvrdepresionestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcarasvrdepresioninestable
    

    elif tipopaciente == "bipolar":
        tipolayout = "layoutresultadosbipolar.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcarasvrbipolarestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcarasvrbipolarinestable


    elif tipopaciente == "esquizofrenia":
        tipolayout = "layoutresultadosesquizofrenia.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcarasvresquizofreniaestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcarasvresquizofreniainestable


    elif tipopaciente == "esquizoafectivo":
        tipolayout = "layoutresultadosesquizoafectivo.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcarasvresquizoafectivoestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcarasvresquizoafectivoinestable

    # buscar aciertos por emocion
    aciertosneutral = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "0")
    countaciertosneutral = len(aciertosneutral)
    porcentajeneutral = (countaciertosneutral * 100 )/ 4

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

    return render_template('layoutresultadosappcarasvr.html', porcentajes=porcentajes, datosappcaras=datosappcaras, tipolayout=tipolayout,  tipopaciente=tipopaciente, estadopaciente=estadopaciente, idpaciente=idpaciente, nhcpaciente=nhcpaciente, fechacreacion=fechacreacion)


#  fin Resultados Appcarasvr del paciente ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////






#  Descargar Resultados Appcarasvr del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@appcarasestableinestable.route('/descargarresultadospacienteappcarasvr/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=['GET','POST'])
def descargarresultadospacienteappcarasvr(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):

    if tipopaciente == "depresion":
        tipolayout = "layoutresultadosdepresion.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcarasvrdepresionestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcarasvrdepresioninestable
    
    elif tipopaciente == "bipolar":
        tipolayout = "layoutresultadosbipolar.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcarasvrbipolarestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcarasvrbipolarinestable

    elif tipopaciente == "esquizofrenia":
        tipolayout = "layoutresultadosesquizofrenia.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcarasvresquizofreniaestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcarasvresquizofreniainestable

    elif tipopaciente == "esquizoafectivo":
        tipolayout = "layoutresultadosesquizoafectivo.html"
        
        if estadopaciente == "estable":
            nombretablabd = Appcarasvresquizoafectivoestable
        elif estadopaciente == "inestable":
            nombretablabd = Appcarasvresquizoafectivoinestable

    # buscar aciertos por emocion
    aciertosneutral = buscarallaciertospacienteappcaras(nombretablabd, idpaciente, nhcpaciente, "0")
    countaciertosneutral = len(aciertosneutral)
    porcentajeneutral = (countaciertosneutral * 100 )/ 4

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



    if len(nhcpaciente) == 1:
        nhcmodificado = nhcpaciente
        if estadopaciente == "estable":
            codigoaplicacion = "RFIEXXXXX"
        elif estadopaciente == "inestable":
            codigoaplicacion = "RFIIXXXXX"
        codigocreado = codigoaplicacion + nhcmodificado
        codigo = codigocreado
    
    elif len(nhcpaciente) == 2:
        nhcmodificado = nhcpaciente
        if estadopaciente == "estable":
            codigoaplicacion = "RFIEXXXX"
        elif estadopaciente == "inestable":
            codigoaplicacion = "RFIIXXXX"
        codigocreado = codigoaplicacion + nhcmodificado
        codigo = codigocreado

    elif len(nhcpaciente) == 3:
        nhcmodificado = nhcpaciente
        if estadopaciente == "estable":
            codigoaplicacion = "RFIEXXX"
        elif estadopaciente == "inestable":
            codigoaplicacion = "RFIIXXX"
        codigocreado = codigoaplicacion + nhcmodificado
        codigo = codigocreado

    elif len(nhcpaciente) == 4:
        nhcmodificado = nhcpaciente
        if estadopaciente == "estable":
            codigoaplicacion = "RFIEXX"
        elif estadopaciente == "inestable":
            codigoaplicacion = "RFIIXX"
        codigocreado = codigoaplicacion + nhcmodificado
        codigo = codigocreado

    elif len(nhcpaciente) >= 4:
        nhcmodificado = nhcpaciente[-4:]
        if estadopaciente == "estable":
            codigoaplicacion = "RFIEXX"
        elif estadopaciente == "inestable":
            codigoaplicacion = "RFIIXX"
        codigocreado = codigoaplicacion + nhcmodificado
        codigo = codigocreado



    fecha = datetime.datetime.today().strftime('%d-%m-%Y')
    hora = datetime.datetime.today().strftime('%H-%M-%S')

    # generar el pdf, ya sea que se descarge en la carpeta de descargas o para guardar en el escritorio

    # datos del gráfico

    emociones = ['Neutral', 'Sorpresa', 'Miedo', 'Ira', 'Asco', 'Alegría', 'Tristeza']
    porcentajes = [porcentajeneutral, porcentajesorpresa, porcentajemiedo, porcentajeira, porcentajeasco, porcentajealegria, porcentajetristeza]
    posicion = [0, 1, 2, 3, 4, 5, 6]

    #plt.bar(emociones, porcentajes, color='royalblue', alpha=0.7)
    plt.bar(emociones, porcentajes, color=["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#cd3e95", "#cd763e"], alpha=0.7)
    #plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plt.yticks([0, 12.5, 25, 37.5, 50, 62.5, 75, 87.5, 100])
    plt.xlabel('Emociones')
    plt.ylabel('Porcentaje (%)')
    plt.title('Porcentaje de aciertos en cada una de las emociones')

    # Creacion de labels para ponerlos encima de las barras los porcentajes
    label = [str(porcentajeneutral) + '%', str(porcentajesorpresa) + '%', str(porcentajemiedo) +'%', str(porcentajeira) +'%', str(porcentajeasco) +'%', str(porcentajealegria) +'%', str(porcentajetristeza) +'%']
    
    # Poner el texto encima de cada barra
    for i in range(len(emociones)):
        plt.text(x = posicion[i]-0.25 , y = porcentajes[i]+1, s = label[i], size = 8)

    # Ajustar marjenes de la grafica
    #plt.subplots_adjust(bottom= 0.2, top = 0.98)
    
    # guardar la imagen
    plt.savefig('pdf/grafico.png')
    #plt.savefig(f'pdf/{ codigo }.png')
    plt.clf()
    
    # creacion del pdf
    #c = canvas.Canvas("pdf/grafico.pdf", pagesize=A4)
    c = canvas.Canvas(f"pdf/{ codigo }.pdf", pagesize=A4)

    grafico = ImageReader('pdf/grafico.png')
    #grafico = ImageReader(f'pdf/{ codigo }.png')
    #c.drawImage(grafico,   0*mm,   0*mm, width=190*mm,   preserveAspectRatio=True)
    c.drawImage(grafico,   30*mm,   130*mm, width=160*mm,   preserveAspectRatio=True)

    c.setFont('Helvetica', 12)

    c.drawString(50, 410, "En el programa de 'Reconocimiento Facial de Emociones en Realidad Virtual Inmersiva',")
    c.drawString(50, 395, f"el participante con código: { codigo }, ha conseguido los porcentajes de aciertos para ")
    c.drawString(50, 380, f"cada una de las emociones arriba indicadas.")

    c.setFont('Helvetica', 8)
    c.drawString(50, 50, f"Documento generado con fecha { fecha } a las { hora }.")

    c.save()


    # copiar el archivo en escritorio con fecha y hora

    #rutadesktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    rutadesktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
    rutadesktoparchivo = os.path.join(rutadesktop, f'{ codigo }.pdf')


    #shutil.copy(f'pdf/{ codigo }.pdf', os.path.join(rutadesktop, f'{ codigo }_Fecha_'+ fecha + '_Hora_'+ hora +'.pdf'))
    shutil.copy(f'pdf/{ codigo }.pdf', os.path.join(rutadesktop, codigo + '_Fecha_'+ fecha + '_Hora_'+ hora +'.pdf'))



    #eliminar el pdf de la carpeta image para que no se sature con archivos innecesarios
    os.remove(f'pdf/{ codigo }.pdf')


    flash(f"Se ha guardado el archivo '{ codigo }_Fecha_{ fecha }_Hora_{ hora }.pdf' en la carpeta 'Descargas' con los resultados de la 'Aplicación de Reconocimiento Facial en Realidad Virtual Inmersiva', para el paciente con NHC: { nhcpaciente } en estado { estadopaciente }.", category="crear")

    return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))


#  fin descargar Resultados Appcarasvr del paciente ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




















#  App casco ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




@appcarasestableinestable.route('/emotivpro/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=['GET','POST'])
def emotivpro(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
        

    Popen("start EmotivPRO.exe ", shell= True)
    
    return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))








#  fin App pulsera ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////






#  App pulsera ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




@appcarasestableinestable.route('/empatica/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=['GET','POST'])
def empatica(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    

    Popen("start main.exe ", shell= True)
    
    return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))








#  fin App pulsera ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# reinicio app caraspantalla ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Para reinicio un paciente por completo

@appcarasestableinestable.route('/borrardatospacienteappcaraspantalla/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=["GET", "POST"])
def borrardatospacienteappcaraspantalla(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    # colocar los formulario y escalas que se desean eliminar
        
    if tipopaciente == "depresion":
        if estadopaciente == "estable":
            listaappcaras = [Appcaraspantalladepresionestable]
        elif estadopaciente == "inestable":
            listaappcaras = [Appcaraspantalladepresioninestable]

    elif tipopaciente == "bipolar":
        if estadopaciente == "estable":
            listaappcaras = [Appcaraspantallabipolarestable]
        elif estadopaciente == "inestable":
            listaappcaras = [Appcaraspantallabipolarinestable]

    elif tipopaciente == "esquizofrenia":
        if estadopaciente == "estable":
            listaappcaras = [Appcaraspantallaesquizofreniaestable]
        elif estadopaciente == "inestable":
            listaappcaras = [Appcaraspantallaesquizofreniainestable]

    elif tipopaciente == "esquizoafectivo":
        if estadopaciente == "estable":
            listaappcaras = [Appcaraspantallaesquizoafectivoestable]
        elif estadopaciente == "inestable":
            listaappcaras = [Appcaraspantallaesquizoafectivoinestable]

    # borra los todos los datos del paciente de la aplicacion caras (sacar las escalas de las listas anteriores)
    for appcara in listaappcaras:
        borrarappcaras(appcara, idpaciente, nhcpaciente)

    flash ("Se han borrado los datos y reiniciado la Aplicación Caras Pantalla correctamente", category="borrar")
    return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))



# fin reinicio appcaraspantalla ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# reinicio app carasvr ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Para reinicio un paciente por completo

@appcarasestableinestable.route('/borrardatospacienteappcarasvr/<string:tipopaciente>/<string:estadopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=["GET", "POST"])
def borrardatospacienteappcarasvr(tipopaciente="", estadopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    # colocar los formulario y escalas que se desean eliminar
        
    if tipopaciente == "depresion":
        if estadopaciente == "estable":
            listaappcaras = [Appcarasvrdepresionestable]
        elif estadopaciente == "inestable":
            listaappcaras = [Appcarasvrdepresioninestable]

    elif tipopaciente == "bipolar":
        if estadopaciente == "estable":
            listaappcaras = [Appcarasvrbipolarestable]
        elif estadopaciente == "inestable":
            listaappcaras = [Appcarasvrbipolarinestable]

    elif tipopaciente == "esquizofrenia":
        if estadopaciente == "estable":
            listaappcaras = [Appcarasvresquizofreniaestable]
        elif estadopaciente == "inestable":
            listaappcaras = [Appcarasvresquizofreniainestable]

    elif tipopaciente == "esquizoafectivo":
        if estadopaciente == "estable":
            listaappcaras = [Appcarasvresquizoafectivoestable]
        elif estadopaciente == "inestable":
            listaappcaras = [Appcarasvresquizoafectivoinestable]

    # borra los todos los datos del paciente de la aplicacion caras (sacar las escalas de las listas anteriores)
    for appcara in listaappcaras:
        borrarappcaras(appcara, idpaciente, nhcpaciente)

    flash ("Se han borrado los datos y reiniciado la Aplicación Caras VR correctamente", category="borrar")
    return redirect(url_for('listaformulariospaciente', tipopaciente=tipopaciente, idpaciente = idpaciente, nhcpaciente = nhcpaciente, fechacreacion=fechacreacion))



# fin reinicio appcaraspantalla ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
























# borrado completo del paciente ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Para borrar un paciente por completo

@appcarasestableinestable.route('/borrarpaciente/<string:tipopaciente>/<int:idpaciente>/<string:nhcpaciente>/<string:fechacreacion>/', methods=["GET", "POST"])
def borrarpaciente(tipopaciente="", idpaciente=None, nhcpaciente="", fechacreacion=""):
    # colocar los formulario y escalas que se desean eliminar
        
    if tipopaciente == "depresion":
        listaescalas = [Formularioregistrodepresion, Formularioantecedentesdepresionestable, Formularioantecedentesdepresioninestable, Escalaminicertsdepresionestable, Escalaius12depresionestable, Escalaebrddepresionestable, Escalabdiiidepresionestable, Escalashortstairdepresionestable, Escalahrsddepresionestable, Escalapanasdepresionestable, Escalafastdepresionestable, Escalawhoqoldepresionestable, Escalaeeagdepresionestable, Cuestionarioavataresdepresionestable, Escalaminicertsdepresioninestable, Escalaius12depresioninestable, Escalaebrddepresioninestable, Escalabdiiidepresioninestable, Escalashortstairdepresioninestable, Escalahrsddepresioninestable, Escalapanasdepresioninestable, Escalafastdepresioninestable, Escalawhoqoldepresioninestable, Escalaeeagdepresioninestable, Cuestionarioavataresdepresioninestable]
        listaappcaras = [Appcaraspantalladepresionestable, Appcarasvrdepresionestable, Appcaraspantalladepresioninestable, Appcarasvrdepresioninestable]

    elif tipopaciente == "bipolar":
        listaescalas = [Formularioregistrobipolar, Formularioantecedentesbipolarestable, Formularioantecedentesbipolarinestable, Escalamadrsbipolarestable, Escalaymrsbipolarestable, Escalapanasbipolarestable, Escalafastbipolarestable, Escalawhoqolbipolarestable, Escalaeeagbipolarestable, Cuestionarioavataresbipolarestable, Escalamadrsbipolarinestable, Escalaymrsbipolarinestable, Escalapanasbipolarinestable, Escalafastbipolarinestable, Escalawhoqolbipolarinestable, Escalaeeagbipolarinestable, Cuestionarioavataresbipolarinestable]
        listaappcaras = [Appcaraspantallabipolarestable, Appcarasvrbipolarestable, Appcaraspantallabipolarinestable, Appcarasvrbipolarinestable]

    elif tipopaciente == "esquizofrenia":
        listaescalas = [Formularioregistroesquizofrenia, Formularioantecedentesesquizofreniaestable, Formularioantecedentesesquizofreniainestable, Escalapanssesquizofreniaestable, Escalapanasesquizofreniaestable, Escalafastesquizofreniaestable, Escalawhoqolesquizofreniaestable, Escalaeeagesquizofreniaestable, Cuestionarioavataresesquizofreniaestable, Escalapanssesquizofreniainestable, Escalapanasesquizofreniainestable, Escalafastesquizofreniainestable, Escalawhoqolesquizofreniainestable, Escalaeeagesquizofreniainestable, Cuestionarioavataresesquizofreniainestable]
        listaappcaras = [Appcaraspantallaesquizofreniaestable, Appcarasvresquizofreniaestable, Appcaraspantallaesquizofreniainestable, Appcarasvresquizofreniainestable]


    elif tipopaciente == "esquizoafectivo":
        listaescalas = [Formularioregistroesquizoafectivo, Formularioantecedentesesquizoafectivoestable, Formularioantecedentesesquizoafectivoinestable, Escalapanssesquizoafectivoestable, Escalamadrsesquizoafectivoestable, Escalaymrsesquizoafectivoestable, Escalapanasesquizoafectivoestable, Escalafastesquizoafectivoestable, Escalawhoqolesquizoafectivoestable, Escalaeeagesquizoafectivoestable, Cuestionarioavataresesquizoafectivoestable, Escalapanssesquizoafectivoinestable, Escalamadrsesquizoafectivoinestable, Escalaymrsesquizoafectivoinestable, Escalapanasesquizoafectivoinestable, Escalafastesquizoafectivoinestable, Escalawhoqolesquizoafectivoinestable, Escalaeeagesquizoafectivoinestable, Cuestionarioavataresesquizoafectivoinestable]
        listaappcaras = [Appcaraspantallaesquizoafectivoestable, Appcarasvresquizoafectivoestable, Appcaraspantallaesquizoafectivoinestable, Appcarasvresquizoafectivoinestable]

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



@appcarasestableinestable.route('/exportarbase')
def exportarbase():

    # colocar la ruta donde se crea el directorio
    parent_dir = 'c:/'
    directory1 = 'Registro-AppCaras-Estable-Inestable'
    path1 = os.path.join(parent_dir, directory1)

    fechaexportacion = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    direcciondestino = os.path.join(path1, 'Base-Datos-Appcaras-Estable-Inestable-' + fechaexportacion)
    if not os.path.exists(direcciondestino):
        os.makedirs(direcciondestino)
        
    shutil.copy('database/dbcarasdatosbipolar.db', direcciondestino)
    shutil.copy('database/dbcarasdatosdepresion.db', direcciondestino)
    shutil.copy('database/dbcarasdatosesquizofrenia.db', direcciondestino)
    shutil.copy('database/dbcarasdatosesquizoafectivo.db', direcciondestino)
    
    flash (f"Se han exportado las bases de datos correctamente en el directorio C:\Registro-AppCaras-Estable-Inestable con fecha: {fechaexportacion} ", category="exportar")
    
    return redirect(url_for('inicio'))




# fin Boton exportar base datos ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////








# Boton cerrar programa ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Para cerrar el programa y el navegador:

@appcarasestableinestable.route('/salir')
def salir():

    Popen('taskkill /F /IM brave.exe', shell=True)
    time.sleep(2)
    Popen('taskkill /F /IM main.exe', shell=True)
    Popen('taskkill /F /IM EmotivPro.exe', shell=True)
    Popen('taskkill /F /IM carasPantalla.exe', shell=True)
    time.sleep(5)

    pid = os.getpid()
    os.kill(pid, signal.SIGINT)

    return


# fin Boton cerrar programa ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


if __name__ == '__main__':
    # crea la base de datos si no se encuentra
    db.create_all()

    # genera un puerto 5004 (metodo en el que se utiliza Popen)
    Popen("start brave -incognito -start-maximized /new_tab 127.0.0.1:5004", shell= True)

    time.sleep(1)

    appcarasestableinestable.run(port=5004, debug=False)


    
    
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


