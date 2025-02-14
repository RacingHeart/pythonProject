def get_mask_card_number(card_number: int) -> str:
    """Пишем функцию, которая скрывает номер карты"""
    str_card_number = str(card_number)
    return f"{str_card_number[:7]}******{str_card_number[-4:]}"


def get_mask_account(mask_account: int) -> str:
    """Пишем функцию, которая скрывает номер счёта"""
    str_mask_account = str(mask_account)
    if len(str(mask_account)) < 4:
        raise ValueError('Отсутствует номер карты')
    else:
        return f"**{str_mask_account[-4:]}"
