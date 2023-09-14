"""
Ce fichier contient les vues pour afficher la liste des profils et les détails d'un profil.
"""
from django.shortcuts import render
from .models import Profile
import sentry_sdk


def index(request):
    """
    Affiche la liste de tous les profils sur la page d'index des profils.

    Args:
        request (HttpRequest): L'objet HttpRequest qui représente la demande HTTP.

    Returns:
        HttpResponse: Une réponse HTTP contenant la liste des profils affichés
        sur la page d'index des profils.
    """

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Affiche les détails d'un profil spécifique sur une page dédiée.

    Args:
        request (HttpRequest): L'objet HttpRequest qui représente la demande HTTP.
        username (str): Le nom d'utilisateur du profil à afficher.

    Returns:
        HttpResponse: Une réponse HTTP contenant les détails du profil affiché sur la page dédiée.
    """

    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    message = f"Someone acced to the profil '{username}'"
    sentry_sdk.capture_message(message, level="info")
    return render(request, 'profiles/profile.html', context)
