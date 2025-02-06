def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список операций по значению ключа 'state'."""
    return [operation for operation in operations if operation.get("state") == state]