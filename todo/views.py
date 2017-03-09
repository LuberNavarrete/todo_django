from django.shortcuts import render, render_to_response  
from .models import Categoria, Tarea

def status_report(request):  
	todo_listing = []
	todo_dict = {}
	todo_dict['list_object'] = Tarea.objects.all()
	todo_dict['item_count'] = Tarea.objects.count()
	todo_dict['items_complete'] = Tarea.objects.filter(completado=True).count()
	todo_dict['percent_complete'] = int(float(todo_dict['items_complete']) / todo_dict['item_count'] * 100)
	todo_listing.append(todo_dict)

	return render_to_response('status_report.html', { 'todo_listing': todo_listing })
