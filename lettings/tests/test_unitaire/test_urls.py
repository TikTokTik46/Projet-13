"""
Testes des urls de l'application lettings
"""
import pytest
from django.urls import reverse, resolve
from lettings.views import index, letting
from lettings.models import Address, Letting
from django.http import HttpResponse
from django.test import Client


@pytest.mark.django_db
class TestLettingsUrls:
    def setup_method(self):
        """
        Initialisation des données pour les tests.
        """
        self.client = Client()
        self.address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='ST',
            zip_code=12345,
            country_iso_code='TST'
        )
        self.letting = Letting.objects.create(title='Test Letting',
                                              address=self.address)

    def test_lettings_index_url(self):
        """
        Teste la résolution et la création de l'URL pour la vue
        'lettings_index'.
        """
        url = reverse('lettings:lettings_index')
        assert url == '/lettings/'
        resolver = resolve(url)
        assert resolver.func == index
        response: HttpResponse = self.client.get(url)
        assert response.status_code == 200

    def test_letting_url(self):
        """
        Teste la résolution et la création de l'URL pour la vue 'letting'.
        """
        url = reverse('lettings:letting', args=[self.letting.pk])
        assert url == f'/lettings/{self.letting.pk}/'
        resolver = resolve(url)
        assert resolver.func == letting
        response: HttpResponse = self.client.get(url)
        assert response.status_code == 200
