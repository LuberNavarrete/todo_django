from django.contrib import admin
from .models import Categoria, Tarea

class Categoriaadmin(admin.ModelAdmin):
	search_fields = ['titulo']
	list_display = ('titulo',)

class Tareaadmin(admin.ModelAdmin):
	search_fields = ['titulo','completado','prioridad','categoria','usuario']
	list_display = ('titulo','completado','prioridad','usuario','creado','categoria')
	list_filter = ['titulo','completado','prioridad','categoria','usuario']

admin.site.register(Categoria,Categoriaadmin)
admin.site.register(Tarea,Tareaadmin)