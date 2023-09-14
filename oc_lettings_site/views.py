"""
Ce fichier contient la vue pour afficher la page d'accueil du site.
"""
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from sentry_sdk import capture_message

def index(request):
    """
    Affiche la page d'accueil avec des liens vers les sections "Lettings" et "Profiles".

    Args:
        request (HttpRequest): L'objet HttpRequest qui représente la demande HTTP.

    Returns:
        HttpResponse: Une réponse HTTP affichant la page d'accueil.
    """

    return render(request, 'index.html')


VIEW_ERRORS = {
    404: {'title': _("404 - Page not found"),
          'content': _("Il semble que cette page ait disparu dans "
                       "le cyberespace. Notre équipe de recherche de"
                       " pages égarées est en route, mais en attendant,"
                       " vous pouvez retourner à la sécurité de la page"
                       " d'accueil."), },
    500: {'title': _("Internal error"),
          'content': _("Le serveur a peut-être eu un fou rire, mais il essaie "
                       "de se ressaisir. Revenez plus tard, nous espérons "
                       "qu'il aura retrouvé son sérieux d'ici là."), },
    403: {'title': _("Permission denied"),
          'content': _("Désolé, vous n'avez pas la clé secrète pour cette "
                       "partie du site. C'est comme essayer d'accéder à la "
                       "salle des trésors sans être un pirate. "
                       "Retournez sur la bonne voie."), },
    400: {'title': _("Bad request"),
          'content': _("Il semble que votre demande soit tombée dans le "
                       "mystère des demandes incorrectes."), }, }

def error_view_handler(request, exception, status):
    """Gère les erreurs HTTP en affichant une page d'erreur personnalisée
    et envoie l'erreur à Sentry.."""
    return render(request, template_name='errors.html', status=status,
                  context={'error': exception, 'status': status,
                           'title': VIEW_ERRORS[status]['title'],
                           'content': VIEW_ERRORS[status]['content']})


def error_404_view_handler(request, exception=None):
    """
    Gère les erreurs 404 en utilisant la fonction error_view_handler.
    """
    capture_message("Page not found: %s" % request.path, level="error")
    return error_view_handler(request, exception, 404)

def error_500_view_handler(request, exception=None):
    """
    Gère les erreurs 500 en utilisant la fonction error_view_handler.
    """
    capture_message("Internal server error: %s" % request.path, level="error")
    return error_view_handler(request, exception, 500)
