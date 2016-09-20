from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^report/$', status_report, name = 'report'),
]
