# PokedexFantome
Notre pokedex utilise l'API [pokeapi](https://pokeapi.co/).

## Projet réalisé par :

* Gabriel de La Biche
* Théophile Farvacque
* Hugo Divet

## Installation
**Création de l'environnement virtuel**

Après avoir récuperer notre repos git, il faut créer un environnement virtuel:
```
py -m venv Pokedex
```

On active l'environnement virtuel : 
```
./Pokedex/Scripts/activate
```

On installe tous les paquets nécessaires au bon fonctionnement du projet : 
```
pip install django
cd ./Projet-Pokedex/DjangoPokedex/
pip install requests
```

## Démarrer le projet

On lance le projet avec la commande suivante :
```
py ./manage.py runserver

### Il faut faire la migration avant de pouvoir démarrer le projet
py manage.py migrate
```

## Choix réalisés pendant le projet 
* Traduction des noms des pokémons en français, de même pour les types

* Statistiques clairs pour ne pas perdre l'utilisateur

* Possibilité de naviguer avec une barre de recherche ou bien avec les boutons précédents / suivants

* Recherche possible via le nom ou le numéro du pokedex

