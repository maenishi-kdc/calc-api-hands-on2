import azure.functions as func
from app.calculations import parse_int, divide


def main(req: func.HttpRequest) -> func.HttpResponse:
    a = req.params.get("A")
    b = req.params.get("B")
    try:
        a_i = parse_int(a)
        b_i = parse_int(b)
    except ValueError:
        return func.HttpResponse("400 Invalid input", status_code=400)
    try:
        result = divide(a_i, b_i)
    except ZeroDivisionError:
        return func.HttpResponse("400 Division by zero is not allowed.", status_code=400)
    return func.HttpResponse(str(result), status_code=200, mimetype="text/plain; charset=utf-8")
