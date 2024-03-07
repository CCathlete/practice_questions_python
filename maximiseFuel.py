
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
-- We want to reach as close to n by steps of adding a or b.
"""
class tank:
    def __init__(self, capacity:int):
        self.currently_in = 0
        self.capacity = capacity
        self.half_quantity_flag

    def put_fuel(self, amount_to_put_in:int) -> bool:
        if amount_to_put_in > self.capacity:
            return False
        else:
            self.capacity -= amount_to_put_in
            self.currently_in += amount_to_put_in
        return True
            
    def half_quantity(self) -> None:
        if not self.half_quantity_flag:
            self.currently_in = int(self.currently_in/2)
            self.half_quantity_flag = True

    def decide_which_fuel(self, petrol_amount:int, diesel_amount:int) -> str:
        cap = self.capacity
        take_petrol = cap-petrol_amount >= 0 and\
            cap-petrol_amount < cap-diesel_amount
        take_diesel = cap-diesel_amount >= 0 and\
            cap-petrol_amount >= cap-diesel_amount
        
        if not take_petrol and not take_diesel:
            return 'neither'
        if take_petrol:
            return 'petrol'
        if take_diesel:
            return 'diesel'







class Solution:
    def maximizeTheFuel(self, n:int , A:int , B:int ) -> int :
        amount_left = n
        currently_in = 0
