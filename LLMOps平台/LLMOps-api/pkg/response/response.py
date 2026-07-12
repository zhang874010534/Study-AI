from dataclasses import dataclass,field
from typing import Any

from flask import jsonify

from .http_code import HttpCode

@dataclass()
class Response:
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)

def json(data: Response | None = None):
    return jsonify(data), 200

def success_json(data: Any = None):
    return jsonify(Response(
        code=HttpCode.SUCCESS,
        message="success",
        data=data
    ))

def failure_json(data: Any = None):
    return jsonify(Response(
        code=HttpCode.FAIL,
        message="",
        data=data
    ))

def validation_json(errors: dict | None = None):
    first_key = next(iter(errors))
    if first_key is not None:
        msg = errors.get(first_key)[0]
    else:
        msg = ""
    return jsonify(Response(
        code=HttpCode.VALIDATION_ERROR,
        message=msg,
        data=errors
    ))

def message(code: HttpCode, msg: str = ''):
    return jsonify(Response(
        code=code,
        message=msg,
        data={}
    ))

def success_message(msg: str = ''):
    return message(HttpCode.SUCCESS, msg)

def failure_message(msg: str = ''):
    return message(HttpCode.FAIL, msg)

def not_found_message(msg: str = ''):
    return message(HttpCode.NOT_FOUND, msg)

def unauthorized_message(msg: str = ''):
    return message(HttpCode.UNAUTHORIZED, msg)

def forbidden_message(msg: str = ''):
    return message(HttpCode.FORBIDDEN, msg)