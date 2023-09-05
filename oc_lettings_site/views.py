"""
Ce fichier contient la vue pour afficher la page d'accueil du site.
"""
from django.shortcuts import render


def index(request):
    """
    Affiche la page d'accueil avec des liens vers les sections "Lettings" et "Profiles".

    Args:
        request (HttpRequest): L'objet HttpRequest qui représente la demande HTTP.

    Returns:
        HttpResponse: Une réponse HTTP affichant la page d'accueil.
    """

    return render(request, 'index.html')
