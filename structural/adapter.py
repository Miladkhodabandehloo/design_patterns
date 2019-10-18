class Korean:
    """Korean speaker"""

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class British:
    """English speaker"""

    def __init__(self):
        self.name = "British"

    # Note the different method name here!
    def speak_english(self):
        return "Hello!"


class Adapter:
    def __init__(self, obj):
        self.obj = obj

    def speak(self):
        method_name = "speak_" + self.obj.__class__.__name__.lower()
        return getattr(self.obj, method_name)()


a = Adapter(obj=Korean())
print(a.speak())
