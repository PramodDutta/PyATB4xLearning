# Fixture - Concept in python
# You can use the fixture
# context to the test.
# Similar - pre condition, post condition.


# Pre Condition - token, booking Id - Fixture
# test_Update_negative 1
# test_Update_postitive 2


import pytest


@pytest.fixture()
def is_married():
    return True


def test_i_need_confirm(is_married):
    assert is_married == False