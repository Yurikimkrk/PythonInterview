"""
6. Проверить на практике возможности полиморфизма.

Необходимо разделить дочерний класс ItemDiscountReport на два класса.

Инициализировать классы необязательно.

Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены.

Далее реализовать выполнение каждой из функции тремя способами.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class ItemDiscountReportName(ItemDiscount):
    def get_parent_data(self):
        print(self.get_name())


class ItemDiscountReportPrice(ItemDiscount):
    def get_parent_data(self):
        print(self.get_price())


PRODUCT1 = ItemDiscountReportName('iPhone 11', 99999)
PRODUCT2 = ItemDiscountReportPrice('Nokia3310', 999)
PRODUCT1.get_parent_data()
PRODUCT2.get_parent_data()

for product in (PRODUCT1, PRODUCT2):
    product.get_parent_data()


def product_handler(product):
    product.get_parent_data()


product_handler(PRODUCT1)
product_handler(PRODUCT2)
