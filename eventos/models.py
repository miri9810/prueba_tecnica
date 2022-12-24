from django.db import models

# Create your models here.
class Eventos(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre del evento', db_index=True)
    inicio = models.DateField(verbose_name='Fecha de apertura')
    fin = models.DateField(verbose_name='Fecha de cierre')
    lugar = models.CharField(max_length=250, verbose_name='Lugar')
    detalle = models.TextField(null=True)
    disponibles = models.IntegerField(default=300)
    vendidos = models.IntegerField(default=0)
    canjeados = models.IntegerField(default=0)
    status_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'eventos'