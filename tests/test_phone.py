import pytest

from src.item import Item
from src.phone import Phone


def test_HW4():
    # HW 4
    phone1 = Phone("iPhone 14", 120000, 5, 2)

    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

    assert phone1.number_of_sim == 2
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

    with pytest.raises(Exception):
        phone1.number_of_sim = 0
    #
    # phone1.number_of_sim = 0
    # # ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.