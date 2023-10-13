"""
Teste de l'url de l'application oc_lettings_site
"""
import pytest
from django.urls import reverse, resolve
from oc_lettings_site.views import index


@pytest.mark.django_db
def test_index_url():
    """
    Teste l'URL de la page d'accueil.
    Vérifie que l'URL correspond à '/' et que la vue associée est bien 'index'.
    """
    url = reverse('index')
    assert url == '/'
    resolver = resolve(url)
    assert resolver.func == index
