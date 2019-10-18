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


def factory(type, *args, **kwargs):
    return globals()[type.capitalize()](*args, **kwargs)


puppy = factory("dog", name="rex")
kittie = factory("cat", name="kittie")
print(puppy.__class__.__name__, kittie.__class__.__name__)
