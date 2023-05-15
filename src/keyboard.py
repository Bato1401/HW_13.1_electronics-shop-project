from src.items import Item


class MixinChL:
    """Класс миксин"""
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class KeyBoard(Item, MixinChL):
    """Класс для клавиатур"""

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

