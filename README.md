# API de médiathèque

## Installation et lancement

Dans PowerShell, depuis le dossier du projet :

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

L’API démarre sur http://127.0.0.1:8000. Swagger est disponible sur http://127.0.0.1:8000/docs.

## Tests

```powershell
.\.venv\Scripts\python.exe -m pytest
```

## Compte de démonstration

- Identifiant : `admin`
- Mot de passe : `Albums2026!`
- Dans Swagger, utiliser **Authorize** pour se connecter. Le jeton expire après 30 minutes.

## Fonctionnalités

- Création, consultation, liste, modification et suppression d’albums.
- Validation du titre, de l’année, de la note et du genre.
- Stockage SQLite persistant dans `albums.db`.
- Lecture publique; création, modification et suppression protégées par jeton.
- Deux tests automatisés : création d’un album et refus sans connexion.

## Non terminé

- Il n’y a qu’un compte de démonstration; l’inscription et le changement de mot de passe ne sont pas implémentés.
- La clé JWT est générée au démarrage. Les jetons en cours sont invalidés si le serveur redémarre; définir la variable d’environnement `SECRET_KEY` permet d’utiliser une clé stable.