'''
Created on Mar 10, 2014

@author: wilfo
'''
from django.conf.urls import patterns, url
from sistema.view.view_login import login_user,registrar_user,activar_cuenta

urlpatterns = patterns('',
    url(r'login_user/$',login_user),
    url(r'activar_usuario/$',activar_cuenta),
    url(r'registrar_user/$',registrar_user),
)