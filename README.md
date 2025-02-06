# Виджет банковского  приложения

## Описание:
Это виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка:
1. Клонируйте репозиторий:
``` git clone https://github.com/RacingHeart/pythonProject.git ```

## Использование:
1. Запустите программу PyCharm
2. Клонируйте репозиторий
3. Вставьте свои данные через 

Примеры использования функций:

```from src.processing import filter_by_state, sort_by_date

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)
```
