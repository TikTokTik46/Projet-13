import pytest
from django.urls import reverse
from lettings.models import Address, Letting

@pytest.mark.django_db
def test_select_letting(client):
    """
    Vérifie que la sélection d'une location affiche les détails de la location
     correctement.
    """
    address = Address.objects.create(
        number=123,
        street='Test Street',
        city='Test City',
        state='ST',
        zip_code=12345,
        country_iso_code='TST'
    )
    letting = Letting.objects.create(title='Test Letting',
                                     address=address)
    response = client.get(reverse('lettings:lettings_index'))
    assert response.status_code == 200
    assert letting.title in str(response.content)
    profile_url = reverse('lettings:letting', args=[letting.pk])
    response = client.get(profile_url)
    assert response.status_code == 200
    assert letting.title in str(response.content)
    assert address.city in str(response.content)