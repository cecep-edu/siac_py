'''
Created on Mar 10, 2014

@author: wilfo
'''
from django.conf.urls import patterns, url
from sistema.view.view_login import login_user,registrar_user,activar_cuenta,logout_user
from sistema.view.view_cargar_escritorio import cargar_user_escritorio,configuracion_user

urlpatterns = patterns('',
    url(r'login_user/$',login_user),
    url(r'logout_user/$',logout_user),
    url(r'activar_usuario/$',activar_cuenta),
    url(r'registrar_user/$',registrar_user),
    url(r'cargar_escritorio/$',cargar_user_escritorio),
    url(r'configuracion_user/$',configuracion_user),
)