import json

from io_lottery.app import app
from tests.unit.test_users import UserPayloadFactory


def test_can_add_user_on_post() -> None:
    with app.test_client() as c:
        result = c.post("/users")
        assert result.status_code == 501


def test_prints_add_user_on_post(capsys) -> None:
    payload = UserPayloadFactory()
    with app.test_client() as c:
        c.post("/users", json=payload)
    actual = capsys.readouterr().out
    expected = f'{json.dumps(sorted(payload))}\n'
    assert actual == expected
