import json

import pytest

from io_lottery.controllers import AddUserController, AddUserRequest
from tests.unit.test_users import UserPayloadFactory


def test_can_instantiate_add_user_controller(capsys) -> None:
    controller = AddUserController()
    payload = UserPayloadFactory()
    request = AddUserRequest(json=payload)
    controller.add(request=request)
    actual = capsys.readouterr().out
    expected = f'{json.dumps(sorted(payload))}\n'
    assert actual == expected


def test_add_user_request_has_json_field() -> None:
    user = UserPayloadFactory()
    request = AddUserRequest(json=user)
    assert request.json
