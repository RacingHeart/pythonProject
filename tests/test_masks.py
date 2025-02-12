from src.masks import get_mask_card_number, get_mask_account
import pytest

def test_get_mask_card_number():
    assert get_mask_card_number(1234567891234567) == '1234567******4567'
    assert get_mask_card_number(987654321987654321) == '9876543******4321'
    with pytest.raises(TypeError):
        get_mask_card_number()


def test_get_mask_account():
    assert get_mask_account(123456) == '**3456'
    assert get_mask_account('987654321') == '**4321'
    with pytest.raises(ValueError):
        get_mask_account(123)