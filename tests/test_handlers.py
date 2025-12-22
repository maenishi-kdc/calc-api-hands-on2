import os
import sys


# Ensure src/ is importable
ROOT = os.path.dirname(os.path.dirname(__file__))
SRC = os.path.join(ROOT, "src")
sys.path.insert(0, SRC)

import pytest


class SimpleReq:
    def __init__(self, params):
        self.params = params


class StubHttpResponse:
    def __init__(self, body: str = "", status_code: int = 200, mimetype: str = None):
        # store as bytes to mimic azure.functions.HttpResponse.get_body()
        self._body = body.encode() if isinstance(body, str) else body
        self.status_code = status_code
        self.mimetype = mimetype

    def get_body(self):
        return self._body


def test_multiply_handler_success():
    # import the module and patch its func.HttpResponse
    import multiply as multiply_module

    multiply_module.func.HttpResponse = StubHttpResponse

    req = SimpleReq({"A": "3", "B": "4"})
    resp = multiply_module.main(req)
    assert resp.status_code == 200
    assert resp.get_body().decode() == "12"


def test_divide_handler_invalid_and_zero():
    import divide as divide_module

    divide_module.func.HttpResponse = StubHttpResponse

    # invalid input
    req_invalid = SimpleReq({"A": "x", "B": "2"})
    resp_invalid = divide_module.main(req_invalid)
    assert resp_invalid.status_code == 400
    assert resp_invalid.get_body().decode() == "400 Invalid input"

    # division by zero
    req_zero = SimpleReq({"A": "3", "B": "0"})
    resp_zero = divide_module.main(req_zero)
    assert resp_zero.status_code == 400
    assert resp_zero.get_body().decode() == "400 Division by zero is not allowed."
