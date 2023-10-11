"""
Testes des vues de l'application lettings
"""
import pytest
from django.urls import reverse
from lettings.models import Address, Letting
from django.http import HttpResponse
from django.test import Client

@pytest.mark.django_db
class TestProfileViews:
    def setup_method(self):
        """
        Initialisation des donnés pour les tests.
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

    def test_index_view(self):
        """
        Teste la vue de la liste des locations. Vérifie que la réponse HTTP a
        le code 200 et que le titre du letting est présent dans le contenu de la réponse.
        """
        response: HttpResponse = self.client.get(
            reverse('lettings:lettings_index'))
        assert response.status_code == 200
        assert 'Test Letting' in str(response.content)

    def test_letting_view(self):
        """
        Teste la vue d'une location. Vérifie que la réponse HTTP a le code 200
        et que le titre du letting est présent dans le contenu de la réponse.
        """
        response: HttpResponse = self.client.get(
            reverse('lettings:letting', args=[self.letting.pk]))
        assert response.status_code == 200
        assert 'Test Letting' in str(response.content)
        assert 'Test Street' in str(response.content)
