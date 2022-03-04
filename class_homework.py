class Calculator:
    def __init__(self, brend, model):
        self.brend = brend
        self.model = model

    def __str__(self):
        return f'{self.brend} {self.model} is ready to work.'

    def add(self, *args):
        self.lst = [i for i in args]
        return sum(self.lst)

    def subtract(self, *args):
        self.int = args[0]
        for i in args[1:]:
            self.int -= i
        return self.int

    def multiply(self, *args):
        self.int = args[0]
        for i in args[1:]:
            self.int *= i
        return self.int

    def divide(self, *args):
        self.int = args[0]
        for i in args[1:]:
            self.int /= i
        return self.int

    def integer_division(self, *args):
        self.int = args[0]
        for i in args[1:]:
            self.int //= i
        return self.int

    def modulo(self, *args):
        self.int = args[0]
        for i in args[1:]:
            self.int %= i
        return self.int

calculator = Calculator('Casio', 2000)

# print(calculator.add(10, 10))
# print(calculator.subtract(20, 5, 1, 3 -10))
# print(calculator.multiply(1, 5, 7, -2))
# print(calculator.divide(100, 3))
# print(calculator.integer_division(20,3))
# print(calculator.modulo(100, 5))

class WashingMachine:
    def __init__(self):
        self.__powder = 1000
        self.__conditioner =  1000

    def show_powder(self):
        return f'Запасы порошка равны {self.__powder} гр.'

    def show_conditioner(self):
        return f'Запасы ополаскивателя равны {self.__conditioner} мл.'

    def __subtract_powder(self, val):
        self.__powder -= val

    def __subtract_conditioner(self, val):
        self.__conditioner -= val

    def wash_clothes(self, powder, conditioner):
        if self.__powder < powder and self.__conditioner < conditioner:
            return f'Для очистки, порошка и ополаскивателся недостаточно. Пополните запасы порошка на {powder - self.__powder} гр. и ополаскивателя на {conditioner - self.__conditioner} мл.'
        elif self.__powder < powder:
            return f'Поршка недостаточно. Пополните его запасы на {powder - self.__powder} гр.'
        elif self.__conditioner < conditioner:
            return f'Ополаскивателя недостаточно. Пополните его запасы на {conditioner - self.__conditioner} мл.'
        else:
            self.__subtract_powder(powder)
            self.__subtract_conditioner(conditioner)
            return 'Процесс очистки завершён'


washer = WashingMachine()
# print(washer.wash_clothes(100, 200))
# print(washer.show_powder())
# print(washer.show_conditioner())
# print(washer.wash_clothes(560, 760))
# print(washer.show_powder())
# print(washer.show_conditioner())
# print(washer.wash_clothes(1000, 1000))

class Publication:
    def __init__(self, name, date, pages, library, type):
        self.name = name
        self.date = date
        self.pages = pages
        self.library = library
        self.type = type

    def get_code_in_library(self):
        return f'{self.library[0:2]}, {self.type}, {self.name[0:2]}, {self.pages}, {self.date}'

class Book(Publication):
    pass
class Magazine(Publication):
    pass

class Newspaper(Publication):
    pass

book = Book('Гарри Поттер', '16 07 2005', '607', 'CoolLib', 'book')
print(book.get_code_in_library())
magazine = Magazine('Человек-Паук', '10 05 2004', '28', 'DC', 'magazine')
print(magazine.get_code_in_library())
news = Newspaper('Вести', '04 03 2022', '1', 'KR', 'newspaper')
print(news.get_code_in_library())