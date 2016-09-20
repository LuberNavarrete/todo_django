from django.contrib import admin
from .models import List, Item

class Listadmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ('title',)

class Itemadmin(admin.ModelAdmin):
	search_fields = ['title','completed','priority','todo_list']
	list_display = ('title','completed','priority','create_date','todo_list')
	list_filter = ['title','completed','priority','todo_list']

admin.site.register(List,Listadmin)
admin.site.register(Item,Itemadmin)