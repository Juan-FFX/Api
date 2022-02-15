from django.db import models

from catalogos.models import Lenguajes, Situacion

from bases_de_datos.models import Base

# Create your models here.

class Sistema (models.Model):
    nombre = models.CharField(max_length=60, blank= False, null= False)
    descripcion = models.TextField(blank= False, null=False)
    situacion = models.OneToOneField(Situacion, on_delete=models.PROTECT)
    servidor = models.CharField(max_length=200,blank= False, null=False)
    lenguaje = models.ForeignKey(Lenguajes, on_delete=models.PROTECT)
    bases_de_datos = models.OneToOneField(Base, on_delete= models.PROTECT)
    dominio = models.CharField(max_length=100,blank= False, null=False)
    path = models.CharField(max_length=200,blank= False, null=False)
    
    
    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'
        ordering = ['id']