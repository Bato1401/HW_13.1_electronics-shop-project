import pytest

from src.keyboard import KeyBoard


@pytest.fixture
def kb():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test__str(kb):
    """Тест инициализации"""
    assert str(kb) == "Dark Project KD87A"


def test_language(kb):
    """Проверка языка по умолчанию"""
    assert str(kb.language) == "EN"


def test_change_lang(kb):
    """Проверка корректной смены языка"""
    kb.change_lang()
    assert str(kb.language) == "RU"


def test_2change_lang(kb):
    """Тест двойной смены языка"""
    kb.change_lang().change_lang()
    assert str(kb.language) == "EN"
