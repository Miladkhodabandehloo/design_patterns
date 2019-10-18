class Dog:
    """A simple dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:
    """A simple dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


class DogFactory:

    def get_pet(self, name):
        return Dog(name=name)

    def get_food(self):
        return "Dog food"


class CatFactory:

    def get_pet(self, name):
        return Dog(name=name)

    def get_food(self):
        return "Dog food"


class PetStore:
    def __init__(self, factory):
        self.factory = factory

    def get_pet(self, name):
        pet = self.factory.get_pet(name=name)
        return pet


dog_store = PetStore(factory=DogFactory())
dog = dog_store.get_pet("puppy")
print(dog.speak())
