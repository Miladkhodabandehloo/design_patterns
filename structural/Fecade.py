class IgnitionSystem:
    @staticmethod
    def produce_spark():
        return True


class Engine:
    def __init__(self):
        self.rpm = 0

    def turn_on(self):
        self.rpm = 2000

    def turn_off(self):
        self.rpm = 0


class FuelTank:
    def __init__(self, level=30):
        self.level = level


class DashboardLight:
    def __init__(self, is_on=False):
        self.is_on = is_on

    def __str__(self):
        return self.__class__.__name__

    def status_check(self):
        if self.is_on:
            print("{}: ON".format(str(self)))
        else:
            print("{}: OFF".format(str(self)))


class HandBrakeLight(DashboardLight):
    pass


class FogLampLight(DashboardLight):
    pass


class Dashboard:
    def __init__(self):
        self.lights = {"handbreak": HandBrakeLight(), "fog": FogLampLight()}


class Car(object):

    def __init__(self):
        self.ignition_system = IgnitionSystem()
        self.engine = Engine()
        self.fuel_tank = FuelTank()
        self.dashboard = Dashboard()

    @property
    def km_per_litre(self):
        return 17.0

    def consume_fuel(self, km):
        litres = min(self.fuel_tank.level, km / self.km_per_litre)
        self.fuel_tank.level -= litres
