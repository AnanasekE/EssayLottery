from factory import DictFactory
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyFloat

from io_lottery.app import add_user, app, get_user, update_user, patch_user, delete_user


class UserPayloadFactory(DictFactory):
    name = FuzzyText()
    last_name = FuzzyText()
    email = FuzzyText()
    age = FuzzyInteger(low=0)
    essays_count = FuzzyInteger(low=0)
    rating = FuzzyFloat(low=0)


def test_returns_sent_user() -> None:
    payload = UserPayloadFactory()
    with app.test_request_context(path="/users", method='POST', json=payload):
        actual = add_user()
    assert actual == payload


def test_returns_sent_user_get() -> None:
    with app.test_request_context(path='/users', method='GET') as c:
        actual = get_user()
        assert actual.status_code == 501


# def test_patch_user() -> None:
#     payload = UserPayloadFactory()
#     with app.test_request_context(path='/users', method='PATCH', json=payload):
#         actual = patch_user()
#         assert actual.status_code == 501

def test_returns_sent_user_post() -> None:
    payload = UserPayloadFactory()
    with app.test_request_context(path='/users', method='POST', json=payload):
        actual = add_user()
        assert actual.status_code == 201


def test_returns_send_user_put() -> None:
    payload = UserPayloadFactory()
    with app.test_request_context(path='/users', method='PUT', json=payload):
        actual = update_user(1)
        assert actual.status_code == 200


def test_returns_sent_user_patch() -> None:
    payload = UserPayloadFactory()
    with app.test_request_context(path='/users', method='PATCH', json=payload):
        actual = patch_user(1)
        assert actual.status_code == 200

# nie działa
def test_returns_sent_user_delete() -> None:
    with app.test_request_context(path='/users', method='DELETE'):
        actual = delete_user(1)
        assert actual.status_code == 204
