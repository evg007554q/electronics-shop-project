import item as item
from src.item import Item

class KeyBoard(Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        # self.__number_of_sim = number_of_sim
        self.__language= 'EN'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language='RU'
        else:
            self.__language = 'RU'
        return self

    @property
    def language(self):
        return self.__language