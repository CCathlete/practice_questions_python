class Solution:
    """Consider a car with a max fuel capacity of n litres. Two infinite-capacity containers are 
    available, one containing petrol and the other containing diesel. Each move allows you to
    transfer a (variable) litres of petrol from the petrol container or b litres of diesel from the 
    diesel container into the car.
    
    The task is to maximise the total fuel in the car, subject to the following conditions:

    1. The total fuel in the car cannot exceed n litres.
    2. Either a litres of petrol or b litres of diesel can be added in one move.
    3. The current fuel level of the car can be decreased by half (round down in the case of float 
    values) at most once.

    The goal  is to formulate an approach that determines the maximum achievable fuel amount in the 
    car.
    """
    def maximizeTheFuel(self, n:int , A:int , B:int ) -> int :
        # code here
