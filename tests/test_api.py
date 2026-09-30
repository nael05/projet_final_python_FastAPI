import pytest
from fastapi.testclient import TestClient

import app.database as database
from app.main import app
from app.security import DEFAULT_PASSWORD, DEFAULT_USERNAME


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(database, "DATABASE_PATH", tmp_path / "test_albums.db")
    with TestClient(app) as test_client:
        yield test_client


def test_create_album_returns_201(client):
    login_response = client.post(
        "/login",
        data={"username": DEFAULT_USERNAME, "password": DEFAULT_PASSWORD},
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]

    response = client.post(
        "/albums",
        json={
            "titre": "Premier album",
            "artiste": "Groupe test",
            "genre": "Rock",
            "annee": 2020,
            "note": 8,
        },
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 201
    assert response.json()["titre"] == "Premier album"
    assert "note_interne" not in response.json()


def test_create_album_without_login_is_refused(client):
    response = client.post(
        "/albums",
        json={
            "titre": "Album interdit",
            "artiste": "Groupe test",
            "genre": "Rock",
            "annee": 2020,
            "note": 8,
        },
    )

    assert response.status_code == 401