from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Usuario

class Doctor(models.Model):
 doctor_id = models.AutoField(primary_key=True)
 doctor_nombre = models.CharField(max_length=100, verbose_name='Nombre del doctor')
 doctor_direccion = models.CharField(max_length=200, verbose_name='Direcicon de la casa del doctor')
 doctor_telefono = models.CharField(max_length=12, verbose_name='Telefono del doctor')

 def __str__(self) -> str:
   fila = self.doctor_nombre
   return fila
class Meta:
       db_table = "doctores"

class Especialidad(models.Model):
 especialidad_id = models.AutoField(primary_key=True)
 especialidad_nombre = models.CharField(max_length=100, verbose_name='Nombre de la  especialidad')
 
 def __str__(self) -> str:
   fila = self.especialidad_nombre
   return fila
class Meta:
       db_table = "especialidades"

class Tiposeguro(models.Model):
 tipo_seguro_id = models.AutoField(primary_key=True)
 tipo_seguro_nombre = models.CharField(max_length=100, verbose_name='Nombre del tipo seguro')
 
 def __str__(self) -> str:
   fila = self.tipo_seguro_nombre
   return fila
class Meta:
       db_table = "Tipos_seguro"

class Tipodocumento(models.Model):
 tipo_documento_id = models.AutoField(primary_key=True)
 tipo_documento_nombre = models.CharField(max_length=100, verbose_name='Nombre del tipo seguro')
 
 def __str__(self) -> str:
   fila = self.tipo_documento_nombre
   return fila
class Meta:
       db_table = "Tipo_documento_identidad"

class Paciente(models.Model):
 paciente_id = models.AutoField(primary_key=True)
 tipo_documento = models.ForeignKey(Tipodocumento,on_delete=models.CASCADE, null=True, blank=True)
 nro_documento = models.CharField(max_length=12, verbose_name='Numero de documento de identidad')
 nombres = models.CharField(max_length=100, verbose_name='Nombre del paciente')
 apellidos = models.CharField(max_length=100, verbose_name='Apellidos del paciente')
 direccion = models.CharField(max_length=200, verbose_name='Direccion del paciente')
 fecha_nacimiento = models.DateTimeField()
 tipo_seguro= models.ForeignKey(Tiposeguro,on_delete=models.CASCADE, null=True, blank=True)
 
 def __str__(self) -> str:
   fila = self.nro_documento
   return fila
class Meta:
       db_table = "pacientes"


class Citas(models.Model):
 cita_id = models.AutoField(primary_key=True)
 paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE, null=True, blank=True)
 fecha_cita = models.DateTimeField()
 especialidad= models.ForeignKey(Especialidad,on_delete=models.CASCADE, null=True, blank=True)
 doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, null=True, blank=True)
 observaciones =  models.CharField(max_length=200, verbose_name='Observaciones')
 username = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True, blank=True)

 def __str__(self) -> str:
   fila = self.paciente
   return fila
class Meta:
       db_table = "citas_medicas"


 