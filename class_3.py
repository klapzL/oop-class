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
    pass

parrot1 = Parrot('G', '2')
cat1 = Cat('F', '3')
dog1 = Dog('S', '6')

class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'Имя: {self.name}\nПол: {self.gender}\nВозраст: {self.age}'

class Employee(Person):
    def __init__(self, name, gender, age, company, position, salary):
        self.company = company
        self.position = position
        self.salary = salary
        super().__init__(name, gender, age)

    def __str__(self):
        return f'{self.company}, {self.position}, {self.salary}'

employee = Employee('Антон', 'Муж', '28', 'Apple Inc.', '', '2000')
print(employee)
        

    