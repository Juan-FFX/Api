from django.db import models

from catalogos.models import LenguajeDb
# Create your models here.

class Base(models.Model):
    descripcion = models.TextField(blank= False, null=False)
    puerto = models.CharField(max_length=150,blank= False, null=False)
    servidor = models.CharField(max_length=150)
    servidor_replica = models.CharField(max_length=150,blank= False, null=False)
    tipo = models.CharField(max_length=50,blank=False,null=False) # Primaria, Secunadria, Replica , etc. 
    lenguaje = models.ForeignKey(LenguajeDb, on_delete=models.PROTECT)
    sql = models.BooleanField(default=True)
    
    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = 'Base'
        verbose_name_plural = 'Bases'
        ordering = ['id']
