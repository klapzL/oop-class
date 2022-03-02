class Car:
    def __init__(self, max_speed, petrol_vol):
        self._max_speed = max_speed
        self.__petrol_vol = petrol_vol
        self._current_speed = 0

    def _show_speed(self):
        return f'Текущая скорость равна: {self._current_speed}'

    def increase_speed(self, val):
        if self._max_speed < int(val) + self._current_speed:
            raise ValueError('Больше максимальной скорости')
        elif int(val) < 0:
            raise ValueError('Значение должно быть положительным')
        else: 
            self._current_speed += int(val)
            return f'Скорость повышена до {self._current_speed}'

    def decrease_speed(self, val):
        if self._current_speed < int(val):
            raise ValueError('Значение больше текущей скорости')
        elif int(val) < 0:
            raise ValueError('Значение должно быть положительным')
        else: 
            self._current_speed -= int(val)
            return f'Скорость понижена до {self._current_speed}'
            
# car1 = Car(217, 90)
# val_increase = input()
# car1.increase_speed(val_increase)
# print(car1.show_curr_speed())
# val_decrease = input()
# car1.decrease_speed(val_decrease)
# print(car1.show_curr_speed())

class Car_(Car):

    def show_speed(self):
        return self._current_speed

    def change_speed(self, val):
        if self._current_speed + val > self._max_speed:
            raise ValueError('Скорость не может быть выше максимальной')
        elif self._current_speed + val < 0:
            self._current_speed = 0
        else:
            self._current_speed += val


car2 = Car_(240,80)
car2.change_speed(50)
print(car2.show_speed())
car2.change_speed(-750)
print(car2.show_speed())
