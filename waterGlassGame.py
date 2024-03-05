from typing import List
class Solution:
    def playOfGlasses(self, c1:int, w1:int, c2:int, w2:int, c3:int, w3:int) -> List[int]:
        class Glass:
            def __init__(self, capacity: int, actual_volume: int) -> None:
                self.capacity = capacity
                self.actual_volume = actual_volume
                self.__amount_left = self.capacity - self.actual_volume
            
            def update_delta(self) -> None:
                self.__amount_left = self.capacity - self.actual_volume
                
            def pour_from(self, other) -> None:
                amount_left = self.__amount_left
                amount_in = other.actual_volume
                if amount_left >= amount_in:
                    self.actual_volume += amount_in
                    other.actual_volume = 0
                    self.update_delta()
                    other.update_delta()
                else:
                    self.actual_volume += amount_left
                    other.actual_volume -= amount_left
                    self.update_delta()
                    other.update_delta()

        a = Glass(c1, w1)
        b = Glass(c2, w2)
        c = Glass(c3, w3)

        i=0
        while i<=10**5:
            b.pour_from(a)
            i += 1
            if i==10**5: break
            c.pour_from(b)
            i += 1
            if i==10**5: break
            a.pour_from(c)
            i += 1
            if i==10**5: break

        return [a.actual_volume, b.actual_volume, c.actual_volume]
    
## Official solution ##
# from typing import List
# class Solution:
#     def playOfGlasses(self, c1: int, w1: int, c2: int, w2: int, c3: int, w3: int) -> List[int]:
#         for i in range(100000):
#             if i % 3 == 0:
#                 a = min(w1, c2 - w2)
#                 w1 -= a
#                 w2 += a
#             if i % 3 == 1:
#                 a = min(w2, c3 - w3)
#                 w2 -= a
#                 w3 += a
#             if i % 3 == 2:
#                 a = min(w3, c1 - w1)
#                 w3 -= a
#                 w1 += a
#         return [w1, w2, w3]

if __name__ == "__main__":
    sol = Solution()
    answer = sol.playOfGlasses(10, 3, 11, 4, 12, 5)
    print(answer)