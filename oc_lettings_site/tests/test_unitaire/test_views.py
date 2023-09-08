"""
Testes des vues de l'application oc_lettings_site
"""
import pytest
from django.urls import reverse
from django.test import Client
from django.http import HttpResponse

@pytest.mark.django_db
def test_index_view():
    """
    Teste la vue de la page d'accueil.
    Vérifie que la page renvoie un code HTTP 200 et contient le texte
    "Welcome to Holiday Homes".
    """
    client = Client()
    url = reverse('index')
    response: HttpResponse = client.get(url)
    assert response.status_code == 200
    assert "Welcome to Holiday Homes" in str(response.content)
