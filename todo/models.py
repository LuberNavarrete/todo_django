from __future__ import unicode_literals
from django.db import models
import datetime
from django.conf import settings

PRIORIDAD = (
	(1, 'Baja'),
	(2, 'Normal'),
	(3, 'Alta'),
)

class Categoria(models.Model):
	titulo = models.CharField(max_length = 100, unique = True)

	def __str__(self):
		return self.titulo
	
	class Meta:
		ordering = ['titulo']

class Tarea(models.Model):
	titulo = models.CharField(max_length = 100)
	creado = models.DateTimeField(default = datetime.datetime.now, editable = False)
	prioridad = models.IntegerField(choices = PRIORIDAD, default = 2)
	completado = models.BooleanField(default = False)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, editable = False)
	categoria = models.ForeignKey(Categoria)

	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ['-prioridad','titulo']