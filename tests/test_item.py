"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("Ноутбук", 5000, 2)


def test_calculate_total_price(item):
    """Проверка общей стоимости имеющихся товаров"""
    assert item.calculate_total_price() == 10000


def test_apply_discount(item):
    """Проверка правильности установки скидки на товар"""
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 2500
