import numpy as np 

class Car():

    """
    Models a car.
    The car's simulation process in the simulation is the method .run().
    
    Arguments:
    -----------
    id (int): A unique id for the car
    gas_required (float): Amount of gallons a car will fill
    lay_time (float): Extra minutes that the car stays at the pump
    gas_station (GasStation): The gas station the cars are going to
    env (simpy.Environment): The simpy environment
    
    """
    
    def __init__(
        self,
        id,
        gas_required,
        lay_time,
        params,
        gas_station,
        env
    ):
        
        self.id = id
        self.gas_required = gas_required
        self.lay_time = lay_time
        self.gas_station = gas_station
        self.env = env
        self.params = params
        
        self.wait_time = np.inf
        self.finished = False
        
        self.action = self.env.process(self.run())
        
    def run(self):
        
        queue_time = self.env.now
        
        print(f'Car {self.id} arrives at {round(queue_time, 2)} minutes')
                
        with self.gas_station.resource.request() as req:
            
            yield req
            
            pump_start_time = self.env.now
            
            print(f'Car {self.id} begins utilizing a pump at {round(pump_start_time, 2)} minutes')

            pump_time = self.gas_required / self.params['pump_rate']
            utilization = max(pump_time, self.lay_time)
            
            yield self.env.timeout(utilization)
            
            pump_end_time = self.env.now
            
            print(f'Car {self.id} leaves its pump at {round(pump_end_time, 2)} minutes')
            
            self.finished = True
            
            self.wait_time = pump_start_time - queue_time
            self.gas_station.minutes_utilized += utilization
            self.gas_station.gallons_sold += self.gas_required

