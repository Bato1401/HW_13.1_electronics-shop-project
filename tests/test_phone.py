import pytest

from phone import Phone


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test__repr_(phone):
    """Тест для repr"""
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"

def test__str_(phone):
    """Тест для str"""
    assert str(phone) == 'iPhone 14'