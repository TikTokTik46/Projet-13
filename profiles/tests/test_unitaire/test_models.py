"""
Testes du modèle de l'application profiles
"""
import pytest
from django.contrib.auth.models import User
from profiles.models import Profile

@pytest.mark.django_db
class TestProfileModel:
    def test_profile_creation(self):
        """
        Teste la création d'un profil utilisateur.
        Vérifie que le profil est bien de type Profile, qu'il est associé à l'utilisateur correct et que la ville favorite est correcte.
        """
        user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        profile = Profile.objects.create(user=user, favorite_city='Test City')
        assert isinstance(profile, Profile)
        assert profile.user == user
        assert profile.favorite_city == 'Test City'

    def test_profile_str_method(self):
        """
        Teste la méthode __str__ du profil utilisateur.
        Vérifie que la méthode renvoie le nom d'utilisateur de l'utilisateur associé au profil.
        """
        user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        profile = Profile.objects.create(user=user, favorite_city='Test City')
        assert str(profile) == 'testuser'
