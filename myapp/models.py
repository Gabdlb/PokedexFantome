from django.db import models

# Create your models here.

class EquipePokemon(models.Model):
    #NomEquipe = models.CharField(max_length=50)
    Pokemon1 = models.IntegerField(max_length=5)
    Pokemon2 = models.IntegerField(max_length=5)
    Pokemon3 = models.IntegerField(max_length=5)
    Pokemon4 = models.IntegerField(max_length=5)
    Pokemon5 = models.IntegerField(max_length=5)
