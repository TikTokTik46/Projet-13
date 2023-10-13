"""
Testes des modèles de l'application lettings
"""
import pytest
from django.core.exceptions import ValidationError
from lettings.models import Address, Letting


@pytest.mark.django_db
class TestAddressModel:
    def test_address_creation(self):
        """
        Teste la création d'une instance de modèle Address valide.
        Vérifie que l'instance est créée avec succès et que sa représentation
        en chaîne de caractères est correcte.
        """
        address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='ST',
            zip_code=12345,
            country_iso_code='TST'
        )

        assert isinstance(address, Address)
        assert str(address) == '123 Test Street'

    def test_invalid_state_code(self):
        """
        Teste la validation du code d'État dans le modèle Address.
        Vérifie qu'une exception ValidationError est levée lorsque le code
        d'État est invalide.
        """
        address = Address(
            number=123,
            street='Test Street',
            city='Test City',
            state='S',
            zip_code=12345,
            country_iso_code='TST'
        )
        with pytest.raises(ValidationError) as context:
            address.full_clean()
        expected_message = {'state': ['Ensure this value has at '
                                      'least 2 characters (it has 1).']}
        assert context.value.message_dict == expected_message


@pytest.mark.django_db
class TestLettingModel:
    """
    Teste la création d'une instance de modèle Letting valide.
    Vérifie que l'instance est créée avec succès et que sa représentation
    en chaîne de caractères est correcte.
    """
    def test_letting_creation(self):
        address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )

        letting = Letting.objects.create(title='Test Letting', address=address)

        assert isinstance(letting, Letting)
        assert str(letting) == 'Test Letting'
