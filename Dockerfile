# Utilisez une image de base avec Python
FROM python:3.8-slim

# Configurez l'environnement
ENV PYTHONUNBUFFERED 1

# Définissez le répertoire de travail
WORKDIR /app

# Copiez les fichiers de dépendances (requirements.txt) dans le conteneur
COPY requirements.txt /app/

# Installez les dépendances
RUN pip install -r requirements.txt

# Copiez le reste de l'application dans le conteneur
COPY . /app/

# Exposez le port sur lequel votre application fonctionne (par défaut : 8000)
EXPOSE 8000

# Commande pour exécuter votre application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
