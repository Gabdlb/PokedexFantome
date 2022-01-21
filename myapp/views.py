from tkinter.font import names
from django.shortcuts import render
from django.shortcuts import render
import random
import requests as re
from .models import EquipePokemon


def index(request):
    url = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151'
    r = re.get(url)
    response = r.json()

    if request.method == 'POST':
        if request.POST.get("Pokemon_Equipe"):
            if request.POST.get("Pokemon") != "0":
                num_pokemon = str(request.POST.get("Pokemon"))
                ajouterEquipe(num_pokemon)
            poke1 = pokemon(EquipePokemon.Pokemon1)
            poke2 = pokemon(EquipePokemon.Pokemon2)
            poke3 = pokemon(EquipePokemon.Pokemon3)
            poke4 = pokemon(EquipePokemon.Pokemon4)
            poke5 = pokemon(EquipePokemon.Pokemon5)
            ArrayEquipe = [poke1, poke2, poke3, poke4, poke5]
            context = {'list': EquipePokemon, 'ArrayEquipe': ArrayEquipe}
            return render(request, 'myapp/equipe.html', context)

    return render(request, 'myapp/equipe.html', response)


def find_pok_order(name):
    url = "https://pokeapi.co/api/v2/pokemon/"
    r = re.get(url + str(name))
    response = r.json()
    pok_order = int(response['id'])

    return pok_order


def pokemon(pok_order):
    if pok_order is None:
        return
    url = "https://pokeapi.co/api/v2/pokemon/"
    urlname = "https://pokeapi.co/api/v2/pokemon-species/"
    urltype = "https://pokeapi.co/api/v2/type/"
    name = ''
    poids = ''
    image = ''
    sprite = ''
    typeFR = ''
    taille = ''
    shiny = ''

    if 1 <= pok_order <= 151:
        r = re.get(url + str(pok_order))
        rname = re.get(urlname + str(pok_order))
        response = r.json()
        responsename = rname.json()
        name = responsename['names'][4]['name']
        image = response['sprites']['other']['official-artwork']['front_default']
        sprite = response['sprites']['front_default']
        types = response['types']
        poids = int(response['weight']) / 10
        taille = int(response['height']) / 10
        shiny = response['sprites']['front_shiny']

        # Traduction des types en francais
        typeFR = []
        for type in types:
            rtype = re.get(urltype + str(type['type']['name']))
            responsetype = rtype.json()
            typeFR.append(responsetype['names'][3]['name'])

    pokemon_list = {'name': name, 'image': image, 'type': typeFR, 'sprite': sprite, 'poids': poids, 'taille': taille,
                    'shiny': shiny}

    return pokemon_list


def home(request):
    try:
        pok_order = find_pok_order(request.POST.get("Pokemon"))
    except:
        pok_order = 1
    # pok_order = 1
    pok_precedent = pok_order - 1
    if pok_precedent < 1:
        pok_precedent = 0
    pok_suivant = pok_order + 1
    if pok_suivant > 151:
        pok_suivant = 0
    tab_pokemon = pokemon(pok_order)
    tab_precedent = pokemon(pok_precedent)
    tab_suivant = pokemon(pok_suivant)
    context = {'name': tab_pokemon['name'], 'image': tab_pokemon['image'], 'type': tab_pokemon['type'],
               'poids': tab_pokemon['poids'], 'taille': tab_pokemon['taille'], 'shiny': tab_pokemon['shiny'],
               'name_precedent': tab_precedent['name'], 'name_suivant': tab_suivant['name'],
               'sprite': tab_pokemon['sprite'],
               'sprite_precedent': tab_precedent['sprite'], 'sprite_suivant': tab_suivant['sprite'],
               'pok_order': pok_order, 'pok_precedent': pok_precedent, 'pok_suivant': pok_suivant}

    return render(request, 'myapp/index.html', context)


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


def equipe(request):
    return render(request, 'myapp/equipe.html')
