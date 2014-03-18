# -*- encoding: utf-8 -*-
'''
Created on Mar 13, 2014

@author: wilfo
'''
import json
from django.http.response import HttpResponse
from django.shortcuts import redirect
def cargar_user_escritorio(request):
    detail = {"user":{"user_k":"1","username":"wilfo","email":"wilfo@hotmail.com","name":"Wilfredo","lastname":"Martel","avatar":"default.png","active":"1"}
              ,"config":{"wallpaper":"resources/wallpapers/2011.jpg"},
              "applications":[{"text":"Hoja de Vida","name":"Hoja de vida","application_k":"6",
                               "application_parent_k":"0","klass":"IAEN.modules.bla.bla...",
                               "description":"Applications catalog",
                               "configurations":"{\"iconCls\":\"groups-icon-16\",\"width\":850,\"height\":480,\"shorcutIconCls\":\"roles-app-shorcut-icon\"}",
                               "active":"1","iconCls":"groups-icon-16","leaf":True}],"success":True}
                               
    json_string = json.dumps(detail)
    #json_string = request.user
    return HttpResponse(json_string)

def configuracion_user(request):
    #return redirect('/')
    detail={"user":"wilfredo","application_k":1,"dock":"bottom","config":{},"success":True,"message":"ok"}
    json_string = json.dumps(detail)
    return HttpResponse(json_string)