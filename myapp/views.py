from django.shortcuts import render
from django.shortcuts import render
import random
import requests as re
from .models import EquipePokemon

# ptite methode pour test l'api, la c juste affichache des 151 pok en console
def index(request):
    url = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151'
    r = re.get(url)
    response = r.json()
    for pokemon in response['results']:
        print(pokemon['name'])

    return render(request, 'myapp/index.html', response)


def ajouterEquipe(id_pokemon):
    if EquipePokemon.Pokemon1 is None:
        EquipePokemon.Pokemon1 = id_pokemon
    elif EquipePokemon.Pokemon2 is None:
        EquipePokemon.Pokemon2 = id_pokemon
    elif EquipePokemon.Pokemon3 is None:
        EquipePokemon.Pokemon3 = id_pokemon
    elif EquipePokemon.Pokemon4 is None:
        EquipePokemon.Pokemon4 = id_pokemon
    elif EquipePokemon.Pokemon5 is None:
        EquipePokemon.Pokemon5 = id_pokemon
    else:
       return False