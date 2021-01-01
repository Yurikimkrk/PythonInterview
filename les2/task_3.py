"""
3. Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'{self.get_name()} стоит {self.get_price()} руб')


PRODUCT = ItemDiscountReport('iPhone 11', 99999)
PRODUCT.get_parent_data()
