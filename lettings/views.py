"""
Ce fichier contient les vues pour afficher la liste des locations et les détails d'une location.
"""
from django.shortcuts import render
from .models import Letting
import sentry_sdk


def index(request):
    """
    Affiche la liste de toutes les locations disponibles sur la page d'accueil.

    Args:
        request (HttpRequest): L'objet HttpRequest qui représente la demande HTTP.

    Returns:
        HttpResponse: Une réponse HTTP contenant la liste des locations
        affichées sur la page d'accueil.
    """

    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Affiche les détails d'une location spécifique sur une page dédiée.

    Args:
        request (HttpRequest): L'objet HttpRequest qui représente la demande HTTP.
        letting_id (int): L'identifiant unique de la location à afficher.

    Returns:
        HttpResponse: Une réponse HTTP contenant les détails de la location
        affichée sur la page dédiée.
    """

    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    message = f"Someone acced to the letting '{letting.title}'"
    sentry_sdk.capture_message(message, level="info")
    return render(request, 'lettings/letting.html', context)
