from django.db import models

# Create your models here.
from django.db import models

class Giocatore(models.Model):
    nome = models.CharField(max_length=50)
    soprannome = models.CharField(max_length=50)
    punti_totalizzati = models.IntegerField(default=0)
    partite_giocate = models.IntegerField(default=0)

    def __str__(self):
        return self.nome + " (" + self.soprannome + ")"

