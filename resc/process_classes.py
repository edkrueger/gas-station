"""
Definition of our sole process class, Car.
"""


import numpy as np


class Car:

    """
    Models a car.
    The car's simulation process in the simulation is the method .run().

    Arguments:
    -----------
    car_id (int): A unique id for the car
    gas_required (float): Amount of gallons a car will fill
    lay_time (float): Extra minutes that the car stays at the pump
    gas_station (GasStation): The gas station the cars are going to
    env (simpy.Environment): The simpy environment

    """

    def __init__(self, car_id, gas_required, lay_time, params, gas_station, env):

        self.car_id = car_id
        self.gas_required = gas_required
        self.lay_time = lay_time
        self.gas_station = gas_station
        self.env = env
        self.params = params

        self.wait_time = np.inf
        self.finished = False

        self.action = self.env.process(self.run())

    def run(self):
        """
        Runs through all processes of a Car at a Gas Station.
        Prints start and end times at pump based on Car's pump rate
        Assignes key metrics about trip to pump

        Yields:
            req (simpy.Resource.request): allows for Car's "use" of Gas_Station resource
            simpy.Environment.timeout:
                Time for current process to run. Accumulates until simulation time reached.
        """

        queue_time = self.env.now

        print(f"Car {self.car_id} arrives at {round(queue_time, 2)} minutes")

        with self.gas_station.resource.request() as req:

            yield req

            pump_start_time = self.env.now

            print(
                f"Car {self.car_id} begins utilizing a pump at {round(pump_start_time, 2)} minutes"
            )

            pump_time = self.gas_required / self.params["pump_rate"]
            utilization = max(pump_time, self.lay_time)

            yield self.env.timeout(utilization)

            pump_end_time = self.env.now

            print(
                f"Car {self.car_id} leaves its pump at {round(pump_end_time, 2)} minutes"
            )

            self.finished = True

            self.wait_time = pump_start_time - queue_time
            self.gas_station.minutes_utilized += utilization
            self.gas_station.gallons_sold += self.gas_required
