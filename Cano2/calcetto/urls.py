from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_giocatori, name='lista_giocatori'),
]
