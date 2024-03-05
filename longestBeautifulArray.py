import math


class Solution:
	def longestBeautifulSubarray(self, n, arr):
		max_beauty_level = 0
		beautifulest_array = []
		for i in range(n):
			piece = arr[:i+1]
			product_of_elements = math.prod(piece)
			factorial_of_len = math.factorial(i+1)
			beauty_level = float(product_of_elements/factorial_of_len)
			if beauty_level >= max_beauty_level:
				beautifulest_array = piece
				max_beauty_level = beauty_level
		return beautifulest_array
        
if __name__ == "__main__":
	print("hi")
	solut = Solution()
	output = solut.longestBeautifulSubarray(5, [3, 4, 1, 5, 2])
	print(output)