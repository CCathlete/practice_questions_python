import math


class Solution:
	def longestBeautifulSubarray(self, n, arr):
		max_beauty_level = 0
		beautifulest_array = []
		for i in range(n):
			piece = arr[:i+1]
			product_of_elements = math.prod(piece)
			beauty_level = float(product_of_elements/(i+1))
			if beauty_level >= max_beauty_level:
				beautifulest_array = piece
				max_beauty_level = beauty_level
		return beautifulest_array
        
if __name__ == "__main__":
	print("hi")
	solut = Solution()
	output = solut.longestBeautifulSubarray(3, [2, 3, 4])
	print(output)