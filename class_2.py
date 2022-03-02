class Car:
    def __init__(self, max_speed, petrol_vol):
        self.__max_speed = max_speed
        self.__petrol_vol = petrol_vol
        self.__curr_speed = 0

    def show_curr_speed(self):
        return f'Текущая скорость равна: {self.__curr_speed}'

    def increase_speed(self, val):
        if self.__max_speed < int(val) + self.__curr_speed:
            raise ValueError('Больше максимальной скорости')
        elif int(val) < 0:
            raise ValueError('Значение должно быть положительным')
        else: 
            self.__curr_speed += int(val)
            return 'Скорость повышена'

    def decrease_speed(self, val):
        if self.__curr_speed < int(val):
            raise ValueError('Значение больше текущей скорости')
        elif int(val) < 0:
            raise ValueError('Значение должно быть положительным')
        else: 
            self.__curr_speed -= int(val)
            return 'Скорость понижена'
            
car1 = Car(217, 90)
val_increase = input()
car1.increase_speed(val_increase)
print(car1.show_curr_speed())
val_decrease = input()
car1.decrease_speed(val_decrease)
print(car1.show_curr_speed())