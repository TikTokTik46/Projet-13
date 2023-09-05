"""
Ce fichier contient les modèles Address et Letting de l'application "lettings".
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse postale.

    Attributes:
        number (PositiveIntegerField): Le numéro de la rue.
        street (CharField): Le nom de la rue.
        city (CharField): Le nom de la ville.
        state (CharField): L'abréviation de l'État ou de la province (2 caractères).
        zip_code (PositiveIntegerField): Le code postal.
        country_iso_code (CharField): Le code ISO du pays (3 caractères).
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

# Modifie l'affichage du nom au pluriel dans le panneau d'administration
    class Meta:
        verbose_name_plural = 'Addresses'


class Letting(models.Model):
    """
    Modèle représentant une location.

    Attributes:
        title (CharField): Le titre de la location.
        address (OneToOneField): L'adresse associée à la location.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
