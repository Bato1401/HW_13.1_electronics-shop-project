import csv


class InstantiateCSVError(Exception):
    def __str__(self):
        print('Файл items.csv поврежден')


class Item:
    """Класс для представления товара в магазине"""
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        self.path = '../src/items.csv'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов")

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
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        """Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        cls.all = []
        try:
            with open(path, encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                if 'name' not in reader.fieldnames or 'price' not in reader.fieldnames or 'quantity' not in reader.fieldnames:
                    raise InstantiateCSVError
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])

        except FileNotFoundError:
            print('Отсутствует файл items.csv')


    @staticmethod
    def string_to_number(number):
        """Возвращает число из числа-строки"""
        if number.isdigit():
            return int(number)
        return int(float(number))

    def __str__(self):
        return self.__name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        return self.quantity + other.quantity

