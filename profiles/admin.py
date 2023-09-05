"""
Configuration de l'administration pour le modèle "Profile".
"""
from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
