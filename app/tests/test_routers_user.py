from datetime import date
from fastapi.testclient import TestClient
from freezegun import freeze_time


@freeze_time('2023-05-10')
def test_freeze_time(client: TestClient):
    assert date.today().year == 2023
    assert date.today().month == 5
    assert date.today().day == 10


def test_create_user(client: TestClient):
    response = client.put(
        "/hello/test",
        json={"dateOfBirth": date(year=2000, month=2, day=2).strftime('%Y-%m-%d')},
    )
    assert response.status_code == 204


def test_update_existing_user(client: TestClient):
    response = client.put(
        "/hello/test",
        json={"dateOfBirth": "2001-02-02"},
    )
    assert response.status_code == 204


@freeze_time('2023-05-10')
def test_create_user_from_future(client: TestClient):
    response = client.put(
        "/hello/test_from_future",
        json={"dateOfBirth": date(year=2030, month=1, day=1).strftime('%Y-%m-%d')},
    )
    assert response.status_code == 422


def test_create_user_with_invalid_dateformat(client: TestClient):
    response = client.put(
        "/hello/test_invalid_dateformat",
        json={"dateOfBirth": date.today().strftime('%m/%d/%Y')},
    )

    assert response.status_code == 422
