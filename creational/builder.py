class Car:
    def __init__(self):
        self.engine = None
        self.body = None
        self.wheels = None

    def set_body(self, body):
        self.body = body

    def set_engine(self, engine):
        self.engine = engine

    def set_wheels(self, wheels):
        self.wheels = wheels


class Director:
    def __init__(self, builder):
        self.builder = builder

    def get_car(self):
        car = Car()
        car.set_body(body=self.builder.get_body())
        car.set_engine(engine=self.builder.get_engine())
        car.set_wheels(wheels=self.builder.get_wheels())
        return car


class Builder:
    def get_body(self):
        pass

    def get_wheels(self):
        pass

    def get_engine(self):
        pass


class ShelbyBuilder(Builder):
    def get_body(self):
        return "shelby body"

    def get_wheels(self):
        return "shelby wheels"

    def get_engine(self):
        return "shelby engine"


class JeepBuilder(Builder):
    def get_body(self):
        return "jeep body"

    def get_wheels(self):
        return "jeep wheels"

    def get_engine(self):
        return "jeep engine"


shelby_director = Director(builder=ShelbyBuilder())
jeep_director = Director(builder=JeepBuilder())
shelby = shelby_director.get_car()
jeep = jeep_director.get_car()

print(shelby.__dict__, jeep.__dict__)
