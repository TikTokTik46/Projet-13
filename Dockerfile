# syntax = docker/dockerfile:1.2
# Utilisez une image de base avec Python
FROM python:3.12-rc-slim

# Configurez l'environnement
ENV PYTHONUNBUFFERED 1

# Récupération de la SECRET_KEY
ARG SECRET_KEY

# Définissez le répertoire de travail
WORKDIR /app

# Copiez les fichiers de dépendances (requirements.txt) dans le conteneur
COPY requirements.txt /app/

# Installez les dépendances
RUN pip install -r requirements.txt

# Copiez le reste de l'application dans le conteneur
COPY . /app/

# Exécutez la commande collectstatic pour collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposez le port sur lequel votre application fonctionne (par défaut : 8000)
EXPOSE 8000

# Commande pour exécuter votre application
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
