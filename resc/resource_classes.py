import simpy

class GasStation():
    
    """
    Models a gas station as a simpy.Resource with a given number of pumps.
    
    Arguments:
    -----------
    num_pumps (int): The number of pumps at the gas station
    env (simpy.Environment): The simpy environment
    """
    
    def __init__(self, num_pumps, env):
        
        self.num_pumps = num_pumps
        
        self.env = env
        
        self.resource = simpy.Resource(self.env, capacity=num_pumps)
        
        self.minutes_utilized = 0
        self.gallons_sold = 0