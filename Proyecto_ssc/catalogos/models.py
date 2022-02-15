from django.db import models


# Create your models here.
class Situacion(models.Model):
    situacion = models.CharField(max_length=50,blank= False, null=False)
 
    
class Lenguajes(models.Model):
    lenguaje = models.CharField(max_length=150,blank= False, null=False)
    framework = models.CharField(max_length=50,blank= False, null=False)
   

class LenguajeDb(models.Model):
    descripcion = models.CharField(max_length=100,blank=False,null=False)
    active = models.BooleanField(default=True, null=True, blank=True)
    
    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = 'Lenguaje de Base de Datos'
        verbose_name_plural = 'Lenguajes de Bases de Datos'
        ordering = ['id']