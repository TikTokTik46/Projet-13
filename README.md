## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Deploiement

#### Fonctionnement du déploiement

Le déploiement de notre application s'appuie sur une chaîne automatisée. GitHub sert de référentiel pour notre code source. CircleCI surveille les mises à jour sur GitHub et construit l'application, garantissant que le code fonctionne correctement. Docker Hub stocke l'image Docker de l'application, qui est prête à être déployée. Enfin, Render permet un déploiement continu, automatiquement déclenché par les mises à jour de Docker Hub, garantissant que les dernières versions de notre application sont toujours disponibles pour nos utilisateurs. Cette approche assure un déploiement fluide et efficace.

#### Configuration requise pour le déploiement

- GitHub : Un compte GitHub pour héberger votre code source.
- CircleCI : Un compte CircleCI pour configurer le processus d'intégration continue.
- Docker Hub : Un compte Docker Hub pour stocker vos images Docker.
- Render : Un compte Render pour déployer votre application.

#### Etapes du déploiement

- Configuration CircleCI : Liez votre compte à votre compte GitHub et ajoutez votre projet. Ajoutez les variables d'environnement (SECRET_KEY, DOCKER_USERNAME, DOCKER_PASSWORD).
- Configuration DockerHub : Modifiez le lien vers votre image DockerHub dans le job "build_docker_image" du fichier de configuration CircleCI (config.yml).
- Configuration Render : Créez un service web en précisant l'adresse de votre image DockerHub. Définissez la variable d'environnement "SECRET_KEY" dans les paramètres. Récupérez l'adresse du Hook et renseignez-la sur votre projet DockerHub.

### Documentation

Pour accéder à une documentation plus détaillée vous pouvez vous rendre à l'adresse suivante.
https://projet-13.readthedocs.io/fr/latest/index.html
