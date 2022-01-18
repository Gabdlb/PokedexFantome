from django.shortcuts import render
from django.shortcuts import render
import random
import requests as re

# ptite methode pour test l'api, la c juste affichache des 151 pok en console
def index(request):
    url = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151'
    r = re.get(url)
    response = r.json()
    for pokemon in response['results']:
        print(pokemon['name'])

    return render(request, 'myapp/index.html', response)

