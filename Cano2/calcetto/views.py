from django.shortcuts import render

from django.shortcuts import render
from .models import Giocatore

def lista_giocatori(request):
    # Queryset ordinato per punti totalizzati
    giocatori = Giocatore.objects.order_by('-punti_totalizzati')
    context = {'giocatori': giocatori}
    return render(request, 'lista_giocatori.html', context)
