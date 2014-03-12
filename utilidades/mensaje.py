# -*- encoding: utf-8 -*-
'''
Created on Mar 8, 2014

@author: wilfo
'''

def correo_institucion():
    return "cielodivino@gmail.com"
def crear(clase):
    return "%s : Se creo satisfactoriamente."%(clase)

def actualziar(clase):
    return "%s : Se actualizo correctamente."%(clase)

def eliminar(clase):
    return "%s : Se elimino correctamente."%(clase)

def listar(clase):
    return "%s : Se listarón correctamente todos los items."%(clase)


def errorSolicitud():
    return "Petición invalida, contáctese con el administrador por favor."

def cuentaActivada():
    return "Su cuenta ha sido activada.Por favor , ingrese al sistema con su usuario y clave."

def cuentaCreada():
    return "Su cuenta ha sido creada.Revise su correo para poder activarla."

def errorCrearCuenta():
    return "Error al crear su cuenta.Contactese con el administrador."

def loginOK():
    return "Ud. se ha logueado correctamente."

def loginIncorrecto():
    return "Usuario y/o contraseña son incorrectos."

def loginNoActivo():
    return "El usuario no ha sido activado.Por favor, revise la bandeja de entrada de su correo y click en el link de activación."
    