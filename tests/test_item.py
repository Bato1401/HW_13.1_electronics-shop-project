import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Ноутбук", 5000, 2)


def test__repr__():
    """Тест для метода __repr__"""
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test__str__():
    """Тест метода __str__"""
    item1 = Item("Ноутбук", 10000, 20)
    assert str(item1) == 'Ноутбук'


def test_calculate_total_price(item):
    """Проверка общей стоимости имеющихся товаров"""
    assert item.calculate_total_price() == 10000


def test_apply_discount(item):
    """Проверка правильности установки скидки на товар"""
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 2500


def test_instantiate_from_csv():
    """Проверка выгрузки данных из файла csv с загрузкой в список"""
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    """Тест перевода строкового файла в int"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.6') == 5
