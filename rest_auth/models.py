from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class User(AbstractUser):
  class Meta:
    db_table = 'auth_user'

class Coordinador(models.Model):
  id = models.AutoField(primary_key=True)
  apellido_paterno = models.CharField(max_length=50)
  apellido_materno = models.CharField(max_length=50)
  nombres = models.CharField(max_length=50)
  codigo_id= models.CharField(max_length=8, unique=True)
  email = models.EmailField(_('email address'), unique=True)
  
  def NombreCompleto(self):
    cadena="{0} {1}, {2}"
    return cadena.format(self.apellido_paterno,self.apellido_materno,self.nombres)
  
  def __str__(self):
    return self.NombreCompleto()

class Curso(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=50)
  fecha_inicio = models.DateField()
  fecha_fin = models.DateField()
  descripcion = models.TextField()
  creditos = models.PositiveIntegerField()
  idioma = models.CharField(max_length=50)
  estado = models.BooleanField(default=True)
  coordinador = models.ForeignKey(Coordinador,null=False,blank=False,on_delete=models.CASCADE)
  
  def __str__(self):
    return "{0} (Coordinador: {1})".format(self.nombre,self.coordinador)