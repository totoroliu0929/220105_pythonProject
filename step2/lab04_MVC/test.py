class Car:
    def __init__(self, maker='', num_of_doors=4,  fuel_type='oil'):
        self.maker, self.num_of_doors,  self.fuel_type = maker, num_of_doors,  fuel_type

    def __repr__(self):
        return 'I\'m a car.'

class Bus:
    def __init__(self, maker='', size=''):
        self.maker, self.size = maker, size

    def __repr__(self):
        return 'I\'m a bus.'

class Truck:
    def __init__(self, maker='', weight=10):
        self.maker, self.weight = maker, weight

    def __repr__(self):
        return 'I\'m a truck.'