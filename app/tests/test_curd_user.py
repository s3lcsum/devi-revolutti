from copy import copy
from datetime import date

from models.user import UserModel
import crud


def test_user_create(db_session):
    assert_date = date(year=2020, month=2, day=2)
    user = UserModel(username="test_user", dateOfBirth=assert_date)
    crud.user.create_or_update(db_session, db_obj=user)

    assert user.username == "test_user"
    assert user.dateOfBirth == assert_date


def tests_user_exists(db_session):
    assert_date = date(year=2020, month=2, day=2)
    user = UserModel(username="test_user", dateOfBirth=assert_date)
    crud.user.create_or_update(db_session, db_obj=user)
    crud.user.create_or_update(db_session, db_obj=user)

    assert user.username == "test_user"
    assert user.dateOfBirth == assert_date


def test_user_get_by_name(db_session):
    assert_date = date(year=2020, month=2, day=2)
    user = UserModel(username="test_user", dateOfBirth=assert_date)
    crud.user.create_or_update(db_session, db_obj=user)

    user2: UserModel = crud.user.get_by_name(db_session, username="test_user")
    assert user == user2
    assert user.dateOfBirth == assert_date


def test_user_update(db_session):
    assert_date = date(year=2020, month=2, day=2)
    user = UserModel(username="test_user", dateOfBirth=assert_date)
    crud.user.create_or_update(db_session, db_obj=user)

    user_copy = copy(user)
    user_copy.dateOfBirth = date(year=1999, month=2, day=2)

    user_updated = crud.user.create_or_update(db_session, db_obj=user_copy)
    assert user_updated.dateOfBirth is not user.dateOfBirth
