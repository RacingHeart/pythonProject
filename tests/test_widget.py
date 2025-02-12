from src.widget import mask_account_card
from src.widget import get_date
import pytest


def test_mask_account_card():
    assert mask_account_card("Счет 11223344556677889900") == 'Счет **9900'
    assert mask_account_card('Mir Pay 1234567891234567') == 'Mir Pay  1234 56** **** 4567'
    with pytest.raises(TypeError):
        mask_account_card(' 123456')

@pytest.mark.parametrize('number_card, result', [
    ('Счет 112233445566778899', 'Счет **8899'),
    ('Visa Gold 1234567891234567', 'Visa Gold  1234 56** **** 4567'),])
def test_mask_account_card(number_card, result):
    assert mask_account_card(number_card) == result

def test_get_date():
    assert get_date('2024-02-11T04:35:54.671407') == '11.02.2024'
    with pytest.raises(ValueError):
        get_date('20240-002-111T04:35:54.671407')
    with pytest.raises(ValueError):
        get_date('T04:35:54.671407')