import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_select_profile(client):
    """
    Vérifie que la sélection d'un profil affiche les détails du profil correctement.
    """
    favorite_city = 'Test City'
    user = User.objects.create_user(username='testuser', password='testpassword')
    Profile.objects.create(user=user, favorite_city=favorite_city)
    response = client.get(reverse('profiles:profiles_index'))
    assert response.status_code == 200
    assert user.username in str(response.content)
    profile_url = reverse('profiles:profile', args=[user.username])
    response = client.get(profile_url)
    assert response.status_code == 200
    assert user.username in str(response.content)
    assert favorite_city in str(response.content)
