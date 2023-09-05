"""
Ce fichier contient le modèle Profile de l'application "profiles".
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle représentant un profil utilisateur personnalisé.

    Ce modèle étend le modèle utilisateur intégré de Django (User) en ajoutant des informations
    supplémentaires telles que la ville favorite de l'utilisateur.

    Attributes:
        user (OneToOneField): Le lien vers l'utilisateur associé à ce profil.
        favorite_city (CharField): La ville favorite de l'utilisateur (facultatif).
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
