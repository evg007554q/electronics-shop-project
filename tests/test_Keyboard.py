import pytest

from src.item import Item
from src.keyboard import KeyBoard



def test_HW5():
    # HW 5
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"


    #
    with pytest.raises(Exception):
        kb.language = 'CH'