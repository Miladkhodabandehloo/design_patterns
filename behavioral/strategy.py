import types

class StrategyExample:
    def __init__(self, name, method=None):
        self.name = name
        if method is not None:
            self.execute = types.MethodType(method, self)

    def execute(self):
        print(self.name)


def method1(self):
    print("%s, %s" % (self.name, "method1"))


def method2(self):
    print("%s, %s" % (self.name, "method2"))


strat = StrategyExample("0")
strat1 = StrategyExample(name=1, method=method1)
strat2 = StrategyExample(name=2, method=method2)

strat.execute()
strat1.execute()
strat2.execute()
