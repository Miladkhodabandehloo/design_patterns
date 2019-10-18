def singleton(cls):
    class SingletonCls(cls):
        _instance = None

        def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super(SingletonCls, cls).__new__(cls)
            return cls._instance

    SingletonCls.__name__ = cls.__name__
    return SingletonCls


@singleton
class Person(object):
    def __init__(self, name):
        self.name = name


p1 = Person(name="p1")
p2 = Person(name="p2")

print(p1.__dict__, p2.__dict__,
      id(p1), id(p2))
