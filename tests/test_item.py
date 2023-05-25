"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)

@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000

def test_calculate_total_price1(item2):
    assert item2.calculate_total_price() == 100000

#Item.pay_rate = 0.8

def test_apply_discount(item1):
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.calculate_total_price() == 160000

def test_HW2(item1):

    # длина наименования товара меньше 10 символов
    item1.name = 'Смартфон'

    assert item1.name == 'Смартфон'

      # длина наименования товара больше 10 символов
    # item1.name = 'СуперСмартфон'
    assert item1.name == 'Смартфон'
    # assert item1.name != 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.
    with pytest.raises(Exception):
        item1.name = 'СуперСмартфон'

    # '../src/items.csv'
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'СмартФон'

    # print(item1.name)
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5.5


def test_HW3():
    # HW 3
    item_hw3 = Item("Смартфон", 10000, 20)
    assert repr(item_hw3) == "Item(Смартфон, 10000, 20)"
    assert str(item_hw3) == 'Смартфон'