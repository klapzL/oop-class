import random

class Player:
    def __init__(self):
        self.playlist = []

    def show_playlist(self):
        print(', '.join(self.playlist))

    def add_to_playlist(self, name):
        self.playlist.append(name)

    def play(self, name):
        if name in self.playlist:
            return f'{name} играет'
        raise ValueError('Файла с таким название не найдено')

    def delete_from_playlist(self, name):
        try:
            self.playlist.remove(name)
        except ValueError:
            raise ValueError('Не найдено')

    def shuffle(self):
        random.shuffle(self.playlist)

class AudioPlayer(Player):
    pass

class VideoPlayer(Player):
    pass

# audio = AudioPlayer()
# audio.add_to_playlist('Drowning')
# audio.add_to_playlist('Increment')
# audio.add_to_playlist('framed')
# audio.add_to_playlist('Dark Beach')
# audio.add_to_playlist('Renee')
# audio.show_playlist()
# audio.delete_from_playlist('framed')
# audio.show_playlist()
# audio.delete_from_playlist('Renee')
# audio.show_playlist()
# audio.shuffle()
# audio.show_playlist()

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'Brand = {self.brand}\nModel = {self.model}'

plane = Plane('Boeing', '737-800')
print(plane)

class Destroyer(Plane):
    def __init__(self, brand, model):
        self.can_fire = True
        super.__init__(brand, model)

class Stelth(Plane):
    def __init__(self, brand, model):
        self.is_visible = False
        super.__init__(brand, model)

class Kukuruznik(Plane):
    def __init__(self, brand, model):
        self.can_fertilize = True
        super.__init__(brand, model)


class Person:
    __last_number = 0

    def __init__(self):
        Person.__last_number += 1
        self.id = Person.__last_number
        self.id

p = Person()
print(p.id)
print(p.id)
print(p.id)