class Vehicle:
    def __init__(self,
                 producer: str,
                 model: str,
                 year: int,
                 tank_capacity: float,
                 tank_level: float,
                 maxspeed: int,
                 fuel_consumption: float,
                 odometer_value: int
                 ):

        self.producer = producer
        self.model = model
        self.year = year
        self.tank_capacity = tank_capacity
        self.tank_level = tank_level
        self.maxspeed = maxspeed
        self.fuel_consumption = fuel_consumption
        self.odometer_value = odometer_value
