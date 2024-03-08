from typing import Self
"""Consider a car with a max fuel capacity of n litres. Two infinite-
capacity containers are available, one containing petrol and the other 
containing diesel. Each move allows you to transfer a (variable) litres 
of petrol from the petrol container or b litres of diesel from the 
diesel container into the car.

The task is to maximise the total fuel in the car, subject to the 
following conditions:

1. The total fuel in the car cannot exceed n litres.
2. Either a litres of petrol or b litres of diesel can be added in one 
move.
3. The current fuel level of the car can be decreased by half (round 
down in the case of float values) at most once.

The goal is to formulate an approach that determines the maximum 
achievable fuel amount in the car.
-- We want to reach as close to n by steps of adding a or b.
"""
class tank:
    def __init__(self, capacity:int=0):
        self.currently_in = 0
        self.capacity = capacity
        self.half_quantity_flag = False

    def put_fuel(self, amount_to_put_in:int) -> bool:
        if amount_to_put_in > self.capacity:
            return False
        else:
            self.currently_in += amount_to_put_in
        return True
            
    def half_quantity(self) -> None:
        if not self.half_quantity_flag:
            self.currently_in = int(self.currently_in/2)
            self.half_quantity_flag = True

    def decide_which_fuel(self, petrol_amount:int, diesel_amount:int) -> str:
        effective_cap = self.capacity - self.currently_in
        is_petrol_possible = effective_cap-petrol_amount >= 0
        is_diesel_possible = effective_cap-diesel_amount >= 0
        petrol_is_better = \
            effective_cap-petrol_amount < effective_cap-diesel_amount
        # If both are possible, we take the one that fills the tank
        # more. If only one is possible, we return its name.
        if is_petrol_possible and is_diesel_possible:
            if petrol_is_better:
                return 'petrol'
            else:
                return 'diesel'
        elif is_petrol_possible:
            return 'petrol'
        elif is_diesel_possible:
            return 'diesel'
        else:
            return 'neither'
        
    def return_a_copy(self, empty_instance:Self) -> Self:
        empty_instance.capacity = self.capacity
        empty_instance.currently_in = self.currently_in 
        # Now it's not empty.
        return empty_instance


class Solution:
    def maximizeTheFuel(self, n:int , A:int , B:int ) -> int :
        tanky = tank(n)
        previous_quantity = None
        current_quantity = tanky.currently_in
        while current_quantity != previous_quantity:
            previous_quantity = tanky.currently_in
            which_fuel = tanky.decide_which_fuel(petrol_amount=A, 
                                                 diesel_amount=B) 
            # During the following condition the quantity will definitely 
            # change unless we've reached the max amount possible.
            if which_fuel == 'neither':
                if not tanky.half_quantity_flag:
                    temp_tanky = tanky.return_a_copy(empty_instance=tank())
                temp_tanky.half_quantity()
                which_fuel = temp_tanky.decide_which_fuel(petrol_amount=A, 
                                                          diesel_amount=B) 
                if(which_fuel == 'petrol'):
                    temp_tanky.put_fuel(A)
                elif(which_fuel == 'diesel'):
                    temp_tanky.put_fuel(B)
                if tanky.currently_in < temp_tanky.currently_in:
                    tanky = temp_tanky
            elif(which_fuel == 'petrol'):
                tanky.put_fuel(A)
            elif(which_fuel == 'diesel'):
                tanky.put_fuel(B)
            current_quantity = tanky.currently_in
        # We've reached the point of max fuel.
        return current_quantity

if __name__ == '__main__':
    sol = Solution()
    N = 11
    A = 20
    B = 2
    max_fuel = sol.maximizeTheFuel(N, A, B)
    print(max_fuel)

        
        
        
        
        
        
        
        

