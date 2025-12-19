def parse_int(value: str) -> int:
    if value is None:
        raise ValueError("missing")
    try:
        return int(value)
    except Exception:
        raise ValueError("invalid")


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    result = a / b
    if result.is_integer():
        return int(result)
    return result
