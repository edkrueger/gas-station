# Applied Machine Learning Models Using a Simulated Gas Station

Part 1 of 2 discussing the power of creating and running simulations to gather data mimicing that of the real world.

### Why Simulate?
Many programmers new to the world of machine learning typically have an attitude that it will solve all of their business or research problems. Not so! They fail to realize the importance of having complete and robust data in order to properly train a model. "Complete data?" you say? "No such thing!" This is true. When modeling a real-world situation, that is exactly what we are doing -- creating a representative _model_ of reality, not replicating it completely.

Say you expect customers to behave a certain way on your platform or sensors to indicate an expected range of values. What happens when they don't? Do you know how your product will react to incorrect user input? Or react to an environment out of your sensor's calibrated bounds? You might have a reasonable suspicion, but in order to confirm your suspicions about your model's ability to handle these situations, you must simulate!

Simulations are used in a wide array of industries for any number of purposes. Ports might use simulations to plan for ship capacity. Real Estate developers might simulate expected capital expenditure (CapEx) when deciding where to build their next project. The choices are limitless. However, incorporating subject expertise into any model complex enough to fit data is impossible. This is a major machine learning problem. With increased flexibility we lose interpretablility if fed overly specific and fine-tuned information from a simulation.

So, what do we do to avoid this? The most obvious solution is to use the data we _do_ have to inform the behaviors of our simulation! 

### Why a Gas Station?
Say we own a gas station. What sort of questions should a burgeoning gas station tycoon be asking themselves?
First, how many pumps should our station have? How many pumps is _too_ many pumps? How many gallons on average does each vehicle take and at what rate should our pumps flow to maximize our throughput?

After deliberating
- why distributions - exp, normal, etc.
- look at decision, don't assume decision will effect behavior -- by nature of problem some things never show up in dataset
    - twice as many pumps, half as much traffic on each. not so, could be a line waiting

### Simpy Overview
##### Environment .env
- flexible enough to gather info but also use env.
- super efficient - uses queue on each resource very quick to insert, __heap__
##### Resources
1. Request/Release
2. Timeout - leaving if wait too long
######## Gas Station
1. Number of Pumps
2. Number Gallons Sold
3. Minutes Utilized
##### Processes
###### Car
1. Gas Required - normally distributed, important but weakest assumption *could be pert/triangle to do later*
    - 
2. Lay Time - time between when cars pull up to join the queue. 
    - could be easily calibrated    



