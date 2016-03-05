from app import app
import pytest


@pytest.fixture
def apps():
    return app.test_client()


def test_home_sites_should_have_Henrique_Lopes_in_title(apps):
    result = apps.get("/")
    assert "<title>Henrique Lopes | Home</title>" in str(result.data)


def test_books(apps):
    result = apps.get("/")
    assert "Pai Rico Pai Probre" in str(result.data)


def test_where_to_find_me(apps):
    result = apps.get("/")
    str_data = str(result.data)
    assert "GitHub" in str_data
    assert "Delicious" in str_data
    assert "Twitter" in str_data
    assert "Linkedin" in str_data
