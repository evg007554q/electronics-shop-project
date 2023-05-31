import csv
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.base_price = price
        self.quantity = quantity

        Item.all.append(self)

    # HW 3
    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})'

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception('Не подходит - надо меньше букв')
        else:
            self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate*self.base_price

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('нельзя было Phone или Item с экземплярами не Phone или Item классов.')
        return  self.quantity + other.quantity

    @staticmethod
    def string_to_number(st_num):
        """статический метод, возвращающий float число из числа-строки"""
        return float(st_num)

    @classmethod
    def instantiate_from_csv(cls):
        """класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""
        # , file_name_svc = '../src/items.csv'
        file_name_svc = os.path.join('../src','items.csv')
        cls.all.clear()
        with open(file_name_svc, newline = '',encoding='utf-8') as cvsfile:
            reader = csv.DictReader(cvsfile)
            for row in reader:
                cls(row['name'],row['price'],row['quantity'])