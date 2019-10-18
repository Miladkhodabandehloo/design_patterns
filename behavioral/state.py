class State:
    name = "state"
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print('Current:', self.name, ' => switched to new state', state.name)
            self.__class__ = state
        else:
            print('Current:', self.name, ' => switching to', state.name, 'not possible.')


class Off(State):
    name = "off"
    allowed = ["on"]


class On(State):
    name = "on"
    allowed = ['off', 'suspend', 'hibernate']


class Suspend(State):
    name = "suspend"
    allowed = ['on']


class Hibernate(State):
    name = "hibernate"
    allowed = ['on']


class Computer:
    def __init__(self, model="DELL"):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


c = Computer()
c.change(Hibernate)
