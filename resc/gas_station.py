import simpy
import numpy as np 

from scipy.stats import expon
from scipy.stats import norm

from resc.process_classes import Car
from resc.resource_classes import GasStation
from resc.utils import validate_params

class Simulator():
    
    def __init__(self, params):
        
        validate_params(params)
        
        self.params = params
        self.env = simpy.Environment()
        self.processes = []
        self.gas_station = None
        
    def set_up_resources(self):
        
        self.gas_station = GasStation(self.params['num_pumps'], self.env)
        
    def schedule_processes(self):

        id = 0

        while True:

            waiting_time = expon.rvs(loc=0, scale=self.params['expected_wait'])

            std_norm = norm.rvs()
            gas_required = std_norm * self.params['gas_required_std'] + self.params['gas_required_std']
            gas_required = max([0, gas_required])

            lay_time = expon.rvs(loc=0, scale=self.params['expected_lay_time'])

            yield self.env.timeout(waiting_time)

            self.processes.append(
                Car(
                    id=id,
                    gas_required=gas_required,
                    lay_time=lay_time,
                    gas_station=self.gas_station,
                    env=self.env,
                    params=self.params
                )
            )

            id += 1
            
    def run(self, v=0):
        self.set_up_resources()
        self.env.process(self.schedule_processes())
        self.env.run(until=self.params['sim_time']);
        
    def report(self):  
        avg_wait_time = np.array([car.wait_time for car in self.processes if car.finished]).mean()

        total_utilization = self.gas_station.minutes_utilized
        percent_utilization = total_utilization / (self.params['sim_time'] * self.gas_station.num_pumps)

        total_gallons_sold = self.gas_station.gallons_sold

        print(f'Average wait time (minutes): {avg_wait_time}')
        print(f'Percent: {percent_utilization}')
        print(f'Total Gallons Sold: {total_gallons_sold}')