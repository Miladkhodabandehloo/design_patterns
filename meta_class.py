# These are equal


# class Foo:
#     attrs = 100
#
#
# Foo1 = type("Foo1", (Foo, ), {"attrs1": 200})
#
# x = Foo1()
# print(x.__class__.__bases__, type(x), x.attrs, x.attrs1, type(Foo))


class Meta(type):
    def __init__(self, name, bases, dict):
        super(Meta, self).__init__(name, bases, dict)
        self.attr = 100


class Foo(metaclass=Meta):
    pass


class Bar(metaclass=Meta):
    pass


y = Bar()
x = Foo()
print(x.attr, y.attr)
print(type(Foo))

