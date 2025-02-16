from datetime import datetime


def mask_account_card(number_card: str) -> str:
    """Функция, возвращающая замаскированный номер карты или счёта"""

    bill = "Счет"
    if bill in number_card:
        return f"Счет **{number_card[-4:]}"
    else:
        list_name_card = number_card.split()
        name_card = []
        for i in list_name_card:
            if i.isalpha():
                name_card+=i + " "
            elif i.isdigit():
                numbers_card = i
        return f'{"".join(name_card)} {numbers_card[0:4]} {numbers_card[4:6]}** **** {numbers_card[-4:]}'


if __name__ == "__main__":
    print(mask_account_card(str("Visa Platinum 2202345612340099")))
    print(mask_account_card(str("Счет 11223344556677889900")))


def get_date(my_date: str) -> str:
    """Функция, принимающая на вход строку и отдает корректный результат"""
    date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))
