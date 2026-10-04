# FastAPI Médiathèque API

**Projet scolaire individuel**
Ce projet a été réalisé dans le cadre de mes études en informatique à Ynov Campus. Je l'ai conçu et développé de manière individuelle pour valider mes compétences en développement backend avec Python.

## Description
Il s'agit d'une API REST de gestion de médiathèque développée avec FastAPI et SQLite. Elle permet la création, la consultation, la modification et la suppression d'albums musicaux (CRUD complet). L'API inclut un système d'authentification par jeton JWT pour sécuriser les routes de modification, ainsi qu'une documentation Swagger interactive.

## Stack Technique
- **Python 3.9+** : Langage de programmation principal.
- **FastAPI** : Framework backend moderne et rapide.
- **Uvicorn** : Serveur ASGI pour FastAPI.
- **SQLite** : Base de données locale légère (`albums.db`).
- **Pydantic** : Validation des données et typage fort.
- **Pytest** : Framework de tests automatisés.

## Prérequis d'installation
- Python 3.9 ou supérieur.
- Pip (gestionnaire de paquets Python).

## Installation et Lancement
Pour installer et lancer le projet en local, suivez ces commandes (dans PowerShell) :

1. Créez et activez un environnement virtuel, puis installez les dépendances :
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

2. Lancez le serveur de développement :
```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

L’API démarrera sur http://127.0.0.1:8000. 
L'interface de test Swagger est disponible sur http://127.0.0.1:8000/docs.

## Compte de démonstration
L'API inclut un utilisateur par défaut pour tester les routes sécurisées via Swagger (bouton **Authorize**) :
- Identifiant : `admin`
- Mot de passe : `Albums2026!`
(Le jeton expire après 30 minutes).

## Tests
Pour lancer les tests automatisés :
```powershell
.\.venv\Scripts\python.exe -m pytest
```

## Arborescence du Projet
```
projet_final_python_FastAPI/
├── app/               # Code source de l'API FastAPI
│   ├── main.py        # Point d'entrée de l'application
│   ├── models.py      # Modèles Pydantic pour la validation
│   ├── routes.py      # Définition des endpoints API
│   ├── security.py    # Logique d'authentification et JWT
│   └── database.py    # Gestion de la connexion SQLite
├── tests/             # Dossier contenant les tests Pytest
├── albums.db          # Base de données SQLite persistante
├── requirements.txt   # Liste des dépendances Python
└── README.md          # Documentation du projet
```