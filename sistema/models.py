# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User,Group


# Create your models here.
class Grupo_Subgrupo(models.Model):
    grupo=models.ForeignKey(Group)
    nombre_subgrupo=models.CharField(max_length=200)
    estado_subgrupo=models.CharField(max_length=5)
    
class Genero(models.Model):
    nombre_genero=models.CharField(max_length=200)
    
    def as_json(self):
        return dict(
            id=self.pk,
            nombre_genero=self.nombre_genero)
    def jsonToClass(self,json):
        self.nombre_genero=json['nombre_genero']

class EstadoCivil(models.Model):
    nombre_civil=models.CharField(max_length=200)
    def as_json(self):
        return dict(
            id=self.pk,
            nombre_civil=self.nombre_civil
            )
    def jsonToClass(self,json):
        self.nombre_civil=json['nombre_civil']

class TipoIdentidad(models.Model):
    nombre_tipoidentidad=models.CharField(max_length=200)
    
    def as_json(self):
        return dict(
            id=self.pk,
            nombre_tipoidentidad=self.nombre_tipoidentidad
            )
    def jsonToClass(self,json):
        self.nombre_tipoidentidad=json['nombre_tipoidentidad']

class Ocupacion(models.Model):
    nombre_ocupacion=models.CharField(max_length=200)
    
    def as_json(self):
        return dict(
            id=self.pk,
            nombre_ocupacion=self.nombre_ocupacion
            )
    def jsonToClass(self,json):
        self.nombre_ocupacion=json['nombre_ocupacion']

class AreaTrabajo(models.Model):
    nombre_area=models.CharField(max_length=200)
    
    def as_json(self):
        return dict(
            id=self.pk,
            nombre_area=self.nombre_area
            )
    def jsonToClass(self,json):
        self.nombre_area=json['nombre_area']

class TipoSangre(models.Model):
    nombre_tiposangre=models.CharField(max_length=200)
    
    def as_json(self):
        return dict(
            id=self.pk,
            nombre_tiposangre=self.nombre_tiposangre
            )
    def jsonToClass(self,json):
        self.nombre_tiposangre=json['nombre_tiposangre']

class Etnia(models.Model):
    nombre_etnia=models.CharField(max_length=200)
    
    def as_json(self):
        return dict(
            id=self.pk,
            nombre_etnia=self.nombre_etnia
            )
    def jsonToClass(self,json):
        self.nombre_etnia=json['nombre_etnia']

class TipoContrato(models.Model):
    nombre_tipocontrato=models.CharField(max_length=200)
    
    def as_json(self):
        return dict(
            id=self.pk,
            nombre_tipocontrato=self.nombre_tipocontrato
            )
    def jsonToClass(self,json):
        self.nombre_tipocontrato=json['nombre_tipocontrato']

class TipoCuentaBanco(models.Model):
    nombre_tipocuenta=models.CharField(max_length=200) #ahorro o crédito

    def as_json(self):
        return dict(
            id=self.pk,
            nombre_tipocuenta=self.nombre_tipocuenta
            )
    def jsonToClass(self,json):
        self.nombre_tipocuenta=json['nombre_tipocuenta']

class TipoEmpresa(models.Model):
    nombre_tipoempresa=models.CharField(max_length=200) #pública o privada

    def as_json(self):
        return dict(
            id=self.pk,
            nombre_tipoempresa=self.nombre_tipoempresa
            )
    def jsonToClass(self,json):
        self.nombre_tipoempresa=json['nombre_tipoempresa']

class TipoFamiliar(models.Model):
    nombre_familiar=models.CharField(max_length=200) #conyuge , vecino , hijo

    def as_json(self):
        return dict(
            id=self.pk,
            nombre_familiar=self.nombre_familiar
            )
    def jsonToClass(self,json):
        self.nombre_familiar=json['nombre_familiar']

class TipoCertificado(models.Model):
    nombre_certificado=models.CharField(max_length=200)

    def as_json(self):
        return dict(
            id=self.pk,
            nombre_certificado=self.nombre_certificado
            )
    def jsonToClass(self,json):
        self.nombre_certificado=json['nombre_certificado']

class TipoCapacitacion(models.Model):
    nombre_capacitacion=models.CharField(max_length=200)

    def as_json(self):
        return dict(
            id=self.pk,
            nombre_capacitacion=self.nombre_capacitacion
            )
    def jsonToClass(self,json):
        self.nombre_capacitacion=json['nombre_capacitacion']
    
class CategoriaEmpresa(models.Model):
    nombre_catempresa=models.CharField(max_length=200) #banco , institu. pública , privada

    def as_json(self):
        return dict(
            id=self.pk,
            nombre_catempresa=self.nombre_catempresa
            )
    def jsonToClass(self,json):
        self.nombre_catempresa=json['nombre_catempresa']

class Persona_NivelInstruccion(models.Model):
    nombre_instruccion=models.CharField(max_length=200) #primaria , secundaria

    def as_json(self):
        return dict(
            id=self.pk,
            nombre_instruccion=self.nombre_instruccion
            )
    def jsonToClass(self,json):
        self.nombre_instruccion=json['nombre_instruccion']

class Persona_Titulo(models.Model):
    nombre_titulo=models.CharField(max_length=200)
    
    def as_json(self):
        return dict(
            id=self.pk,
            nombre_titulo=self.nombre_titulo
            )
    def jsonToClass(self,json):
        self.nombre_titulo=json['nombre_titulo']

class Persona_Especializacion(models.Model):
    nombre_especializacion=models.CharField(max_length=200)

    def as_json(self):
        return dict(
            id=self.pk,
            nombre_especializacion=self.nombre_especializacion
            )
    def jsonToClass(self,json):
        self.nombre_especializacion=json['nombre_especializacion']

class Institucion(models.Model):
    nombre_institucion=models.CharField(max_length=200)
    representante=models.CharField(max_length=200)
    descripcion=models.CharField(max_length=200)
    web=models.CharField(max_length=200) #url de la empresa
    email=models.CharField(max_length=200)
    telf1=models.CharField(max_length=20)
    telf2=models.CharField(max_length=20)
    direccion=models.CharField(max_length=300)
    categoria_empresa=models.ForeignKey(CategoriaEmpresa) #categoría : banco , instit. pública , privada,etc.
    tipo_institucion=models.ForeignKey(TipoEmpresa,null=True,blank=True) #privada , pública
    
    def as_json(self):
        return dict(
            id=self.pk,
            nombre_institucion=self.nombre_institucion,
            representante=self.representante,
            descripcion=self.descripcion,
            web=self.web,
            email=self.email,
            telf1=self.telf1,
            telf2=self.telf2,
            direccion=self.direccion,
            categoria_empresa=self.categoria_empresa,
            tipo_institucion=self.tipo_institucion
            )
    def jsonToClass(self,json):
        self.nombre_institucion=json['nombre_institucion']
        self.representante=json['representante']
        self.descripcion=json['descripcion']
        self.web=json['web']
        self.email=json['email']
        self.telf1=json['telf1']
        self.telf2=json['telf2']
        self.direccion=json['direccion']
        self.categoria_empresa=json['categoria_empresa']
        self.tipo_institucion=json['tipo_institucion']
        

class Pais_Ciudad(models.Model):
    nombre_ciudad=models.CharField(max_length=100)
    pro_ciu=models.ForeignKey('self', null=True, blank=True, related_name='ciudades')
    
    def as_json(self):
        return dict(
            id=self.pk,
            nombre_ciudad=self.nombre_ciudad
            )
    def jsonToClass(self,json):
        self.pro_ciu=json['pro_ciu']
        self.nombre_ciudad=json['nombre_ciudad']

class Persona(models.Model):
    usuario=models.ForeignKey(User,unique=True)
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    direccion=models.TextField(null=True, blank=True)
    telefono=models.CharField(max_length=20)
    celular=models.CharField(max_length=20)
    codigo_postal=models.CharField(max_length=50) #número de la casa.
    doc_identidad=models.CharField(max_length=20) #ruc , cedula lo que sea
    tipo_identidad=models.ForeignKey(TipoIdentidad) #especifíca si es cédula , ruc , etc.
    carne_conadis=models.CharField(max_length=50)
    discapacidad=models.BooleanField() #true or false
    porcentaje_discapacidad=models.DecimalField(max_digits=8,decimal_places=2,default=0)
    nacionalidad=models.CharField(max_length=100) #nacionalidad de la personas
    email_emergencia=models.CharField(max_length=200) #email de emergencia
    telefono_emergencia=models.CharField(max_length=20)
    contacto_emergencia=models.CharField(max_length=200) #nobre de la persona que se contactará
    ciudad_nacimiento=models.ForeignKey(Pais_Ciudad,related_name='ciudad_nacimiento') #con la ciudad se tiene la provincia , país.
    ciudad_residencia=models.ForeignKey(Pais_Ciudad,related_name='ciudad_residencia') #ciudad de donde reside la persona actualmente
    estado_civil=models.ForeignKey(EstadoCivil)
    tipo_sangre=models.ForeignKey(TipoSangre)
    genero=models.ForeignKey(Genero)  #genero de las personas
    etnia=models.ForeignKey(Etnia) # etnia de la persona
    codigo_acceso=models.CharField(max_length=200) #código de acceso de la tarjeta
    foto=models.CharField(max_length=300) #foto de la persona
    fecha_nacimiento=models.DateField(null=True, blank=True)
    fecha_ingreso=models.DateField(auto_now=True)
    estado=models.CharField(max_length=2) #"estado de la persona: A:Activo , I:Inactivo ,etc "
    
    def as_json(self):
        return dict(
            id=self.pk,
            usuario=self.usuario,
            nombre=self.nombre,
            apellido=self.apellido,
            direccion=self.direccion,
            telefono=self.telefono,
            celular=self.celular,
            codigo_postal=self.codigo_postal,
            doc_identidad=self.doc_identidad,
            tipo_identidad=self.tipo_identidad,
            carne_conadis=self.carne_conadis,
            discapacidad=self.discapacidad,
            porcentaje_discapacidad=self.porcentaje_discapacidad,
            nacionalidad=self.nacionalidad,
            email_emergencia=self.email_emergencia,
            telefono_emergencia=self.telefono_emergencia,
            contacto_emergencia=self.contacto_emergencia,
            ciudad_nacimiento=self.ciudad_nacimiento,
            ciudad_residencia=self.ciudad_residencia,
            estado_civil=self.estado_civil,
            genero=self.genero,
            tipo_sangre=self.tipo_sangre,
            etnia=self.etnia,
            codigo_acceso=self.codigo_acceso,
            foto=self.foto,
            fecha_nacimiento=self.fecha_nacimiento
            )
        
    def jsonToClass(self,json):
        self.nombre= json['nombre']
        self.apellido=json['apellido']
        self.direccion=json['direccion']
        self.telefono=json['telefono']
        self.celular=json['celular']
        self.codigo_postal=json['codigo_postal']
        self.doc_identidad=json['doc_identidad']
        self.tipo_identidad=json['tipo_identidad']
        self.carne_conadis=json['carne_conadis']
        self.discapacidad=json['discapacidad']
        self.porcentaje_discapacidad=json['porcentaje_discapacidad']
        self.nacionalidad=json['nacionalidad']
        self.email_emergencia=json['email_emergencia']
        self.telefono_emergencia=json['telefono_emergencia']
        self.contacto_emergencia=json['contacto_emergencia']
        self.ciudad_nacimiento=json['ciudad_nacimiento']
        self.ciudad_residencia=json['ciudad_residencia']
        self.estado_civil=json['estado_civil']
        self.genero=json['genero']
        self.tipo_sangre=json['tipo_sangre']
        self.etnia=json['etnia']
        self.codigo_acceso=json['codigo_acceso']
        self.foto=json['foto']
        self.fecha_nacimiento=json['fecha_nacimiento']



class Persona_Trabajo(models.Model):
    persona=models.ForeignKey(Persona, unique=True)
    lugar_trabajo=models.TextField(null=True, blank=True) #nombre de la empresa de donde labora
    celular_trabajo=models.CharField(max_length=20)
    telefono_trabajo=models.CharField(max_length=20)
    direccion_trabajo=models.TextField(null=True, blank=True)
    email_trabajo=models.CharField(max_length=200)
    telefono_emergencia=models.CharField(max_length=20)
    area_trabajo=models.ForeignKey(AreaTrabajo)
    cargo_trabajo=models.ForeignKey(Ocupacion)
    tipo_contrato=models.ForeignKey(TipoContrato) #tipo de contrato , por contrato , nombramiento
    tipo_empresa=models.ForeignKey(TipoEmpresa)
    nombre_banco=models.ForeignKey(Institucion)
    tipo_cuenta=models.ForeignKey(TipoCuentaBanco)
    numero_cuenta=models.CharField(max_length=50)
    estado_trabajo=models.BooleanField() #estado del trabajo actual , puede que este retirado , etc.
    
    def as_json(self):
        return dict(
            id=self.pk,
            persona=self.persona,
            lugar_trabajo=self.lugar_trabajo,
            celular_trabajo=self.celular_trabajo,
            telefono_trabajo=self.telefono_trabajo,
            direccion_trabajo=self.direccion_trabajo,
            email_trabajo=self.email_trabajo,
            telefono_emergencia=self.telefono_emergencia,
            area_trabajo=self.area_trabajo,
            cargo_trabajo=self.cargo_trabajo,
            tipo_contrato=self.tipo_contrato,
            tipo_empresa=self.tipo_empresa,
            nombre_banco=self.nombre_banco,
            tipo_cuenta=self.tipo_cuenta,
            numero_cuenta=self.numero_cuenta,
            estado_trabajo=self.estado_trabajo
            )
    
    def jsonToClass(self,json):
        self.lugar_trabajo=json['lugar_trabajo']
        self.celular_trabajo=json['celular_trabajo']
        self.telefono_trabajo=json['telefono_trabajo']
        self.direccion_trabajo=json['direccion_trabajo']
        self.email_trabajo=json['email_trabajo']
        self.telefono_emergencia=json['telefono_emergencia']
        self.area_trabajo=json['area_trabajo']
        self.cargo_trabajo=json['cargo_trabajo']
        self.tipo_contrato=json['tipo_contrato']
        self.tipo_empresa=json['tipo_empresa']
        self.nombre_banco=json['nombre_banco']
        self.tipo_cuenta=json['tipo_cuenta']
        self.numero_cuenta=json['numero_cuenta']
        self.estado_trabajo=json['estado_trabajo']
#fin de clases varias

class Persona_Familia(models.Model):
    persona=models.ForeignKey(Persona,unique=False)
    persona_relacion=models.ForeignKey(Persona,related_name='pariente')
    tipo_familiar=models.ForeignKey(TipoFamiliar) #vecino , conyuge , hijo o hija
    

    
    
class Persona_Banco(models.Model):
    persona=models.ForeignKey(Persona,unique=False)
    banco=models.ForeignKey(Institucion,null=True)
    num_cuenta=models.CharField(max_length=100)
    tipo_cuenta=models.ForeignKey(TipoCuentaBanco,null=True,blank=True)
    
    def as_json(self):
        return dict(
           id=self.pk,
           banco=self.banco,
           num_cuenta=self.num_cuenta,
           tipo_cuenta=self.tipo_cuenta
            )
    def jsonToClass(self,json):
        self.banco=json['banco']
        self.num_cuenta=json['banco']
        self.tipo_cuenta=json['tipo_cuenta']

class Persona_Formacion_Academica(models.Model):
    persona=models.ForeignKey(Persona,unique=False)
    nivel_instruccion=models.ForeignKey(Persona_NivelInstruccion)
    institucion=models.ForeignKey(Institucion)
    senescyt_informacion=models.CharField(max_length=400)
    especializacion=models.ForeignKey(Persona_Especializacion)
    anios_aprobados=models.SmallIntegerField()
    titulo=models.ForeignKey(Persona_Titulo)
    pais=models.ForeignKey(Pais_Ciudad)
    
    def as_json(self):
        return dict(
           id=self.pk,
           nivel_instruccion=self.nivel_instruccion,
           institucion=self.institucion,
           senescyt_informacion=self.senescyt_informacion,
           especializacion=self.especializacion,
           anios_aprobados=self.anios_aprobados,
           titulo=self.titulo,
           pais=self.pais
           )
    def jsonToClass(self,json):
        self.nivel_instruccion=json['nivel_instruccion']
        self.institucion=json['institucion']
        self.senescyt_informacion=json['senescyt_informacion']
        self.especializacion=json['especializacion']
        self.anios_aprobados=json['anios_aprobados']
        self.titulo=json['titulo']
        self.pais=json['pais']
        

class Persona_Experiencia_Laboral(models.Model):
    persona=models.ForeignKey(Persona,unique=False)
    actividad=models.CharField(max_length=400) #actividad a realizar
    institucion=models.ForeignKey(Institucion)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    ocupacion=models.ForeignKey(Ocupacion)
    area_trabajo=models.ForeignKey(AreaTrabajo)
    motivo_ingreso=models.CharField(max_length=300)
    motivo_salida=models.CharField(max_length=300)
    
    def as_json(self):
        return dict(
           id=self.pk,
           actividad=self.actividad,
           institucion=self.institucion,
           fecha_inicio=self.fecha_inicio,
           fecha_fin=self.fecha_fin,
           ocupacion=self.ocupacion,
           area_trabajo=self.area_trabajo,
           motivo_ingreso=self.motivo_ingreso,
           motivo_salida=self.motivo_salida
            )
    def jsonToClass(self,json):
        self.actividad=json['actividad']
        self.institucion=json['institucion']
        self.fecha_inicio=json['fecha_inicio']
        self.fecha_fin=json['fecha_fin']
        self.ocupacion=json['ocupacion']
        self.area_trabajo=json['area_trabajo']
        self.motivo_ingreso=json['motivo_ingreso']
        self.motivo_salida=json['motivo_salida']
        
class Persona_Capacitacion(models.Model):
    persona=models.ForeignKey(Persona,unique=False)
    institucion=models.ForeignKey(Institucion)
    evento=models.CharField(max_length=250)
    tipo_capacitacion=models.ForeignKey(TipoCapacitacion)
    tiempo_capacitacion=models.SmallIntegerField()
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    pais=models.ForeignKey(Pais_Ciudad)
    tipo_certificado=models.ForeignKey(TipoCertificado)
    
    def as_json(self):
        return dict(
            id=self.pk,
            institucion=self.institucion,
            evento=self.evento,
            tipo_capacitacion=self.tipo_capacitacion,
            tiempo_capacitacion=self.tiempo_capacitacion,
            fecha_inicio=self.fecha_inicio,
            fecha_fin=self.fecha_fin,
            pais=self.pais,
            tipo_certificado=self.tipo_certificado
            )
    def jsonToClass(self,json):
        self.institucion=json['institucion']
        self.evento=json['evento']
        self.tipo_capacitacion=json['tipo_capacitacion']
        self.tiempo_capacitacion=json['tiempo_capacitacion']
        self.fecha_inicio=json['fecha_inicio']
        self.fecha_fin=json['fecha_fin']
        self.pais=json['pais']
        self.tipo_certificado=json['tipo_certificado']
