class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        print(self.width * self.length)

r1 = Rectangle(5,7)
print(f'{r1.width=}, {r1.length=}')
r1.area()

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f'Привет {self.name}'

d = Person('Михаил Круг')
print(type(d))
print(d.introduce())
d.name = 'Михаил Таль'
print(d.introduce())