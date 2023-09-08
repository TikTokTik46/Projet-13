"""
Testes des urls de l'application profiles
"""
import pytest
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from profiles.models import Profile
from profiles.views import index, profile
from django.http import HttpResponse
from django.test import Client

@pytest.mark.django_db
class TestProfileUrls:
    def setup_method(self):
        """
        Initialisation des données pour les tests.
        """
        self.client = Client()
        self.username = 'testuser'
        self.user = User.objects.create(username=self.username)
        self.profile = Profile.objects.create(user=self.user)

    def test_profiles_index_url(self):
        """
        Teste la résolution et la création de l'URL
        pour la vue 'profiles_index'.
        """
        url = reverse('profiles:profiles_index')
        assert url == '/profiles/'
        resolver = resolve(url)
        assert resolver.func == index
        response: HttpResponse = self.client.get(url)
        assert response.status_code == 200

    def test_profile_url(self):
        """
        Teste la résolution et la création de l'URL pour la vue 'profile'.
        """
        url = reverse('profiles:profile', args=[self.username])
        assert url == f'/profiles/{self.username}/'
        resolver = resolve(url)
        assert resolver.func == profile
        response: HttpResponse = self.client.get(url)
        assert response.status_code == 200




