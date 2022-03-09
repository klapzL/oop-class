from math import pi

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        print('Привет')

class Dog(Animal):
    def make_sound(self, *args):
        print('Гав')
        super().make_sound(*args)

class Cat(Animal):
    def make_sound(self):
        print('Мяу')

class Parrot(Animal):
    def make_sound(self):
        print('привет')

parrot1 = Parrot('G', '2')
cat1 = Cat('F', '3')
dog1 = Dog('S', '6')

animals = [parrot1, cat1, dog1]

# for o in animals:
    # o.make_sound()

class Shape:
    class Square:
        def __init__(self, val):
            self.val = val

        def area(self):
            return f'Площадь квадрта = {self.val ** 2}'

    class Circle:
        def __init__(self, val):
            self.val = val

        def area(self):
            return f'Площадь окружности = {round(self.val ** 2 * pi, 1)}'

    class Rectangle:
        def __init__(self, val1, val2):
            self.val1 = val1
            self.val2 = val2

        def area(self):
            return f'Площадь прямоугольника = {self.val1 * self.val2}'

square = Shape.Square(10)
circle = Shape.Circle(4)
rectangle = Shape.Rectangle(10, 15)
shapes = [square, circle, rectangle]

# for s in shapes:
#     print(s.area())

