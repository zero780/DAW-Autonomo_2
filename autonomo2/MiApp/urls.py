from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.index, name="index"),
    path('usuario1', views.usuario1, name="usuario1")
]

handler404 = 'MiApp.views.handler404'