"""
Testes des vues de l'application profiles
"""
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile
from django.test import Client
from django.http import HttpResponse

@pytest.mark.django_db
class TestProfileViews:
    def setup_method(self):
        """
        Initialisation des données pour les tests.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                            password='testpassword')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Test City')

    def test_index_view(self):
        """
        Teste la vue d'index des profils.
        Vérifie que la page renvoie un code 200 et que le nom d'utilisateur
        est présent dans le contenu.
        """
        response: HttpResponse = self.client.get(reverse('profiles:profiles_index'))
        assert response.status_code == 200
        assert 'testuser' in str(response.content)

    def test_profile_view(self):
        """
        Teste la vue de profil.
        Vérifie que la page renvoie un code 200, que le nom d'utilisateur et
        la ville favorite sont présents dans le contenu.
        """
        response: HttpResponse = self.client.get(reverse('profiles:profile', args=['testuser']))
        assert response.status_code == 200
        assert 'testuser' in str(response.content)
        assert 'Test City' in str(response.content)
