class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        return 'woof woof'

class Cat(Animal):
    def talk(self):
        return 'meow'

def make_animal_talk(animal):
    return animal.talk()
