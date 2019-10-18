class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, new_observer):
        self.observers.append(new_observer)

    def detach(self, existing_observer):
        try:
            self.observers.remove(existing_observer)
        except Exception:
            pass

    def notify(self, modifier=None):
        for observer in self.observers:
            if observer != modifier:
                observer.notify(self)


class Reactor(Subject):
    def __init__(self, name):
        super(Reactor, self).__init__()
        self.name = name
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify()
        return


class Supervisor(object):
    def __init__(self, name):
        self.name = name

    def notify(self, reactor):
        print(self.name, reactor.name, reactor.temperature)


milad = Supervisor(name="milad")
reactor1 = Reactor(name="reactor1")
reactor1.attach(milad)
reactor1.temperature = 10

