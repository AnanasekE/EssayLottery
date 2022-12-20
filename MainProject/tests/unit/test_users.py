from factory import DictFactory
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyFloat

from MainProject.mainproject.app import add_user, app


class UserPayloadFactory(DictFactory):
    name = FuzzyText()
    last_name = FuzzyText()
    email = FuzzyText()
    age = FuzzyInteger(low=0)
    essays_submitted = FuzzyInteger(low=0)
    rating = FuzzyFloat(low=0)


def test_returns_501() -> None:
    payload = UserPayloadFactory()
    with app.test_request_context(data=payload, path='/users', method='POST'):
        actual = add_user()
    assert actual == payload
