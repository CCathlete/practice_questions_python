"""# QUESTION
Largest Continuous Sequence Zero Sum
Find the largest continuous sequence in a array which sums to zero.

Example:
Input: 1,2,-2,4,-4
Output: 2,-2,4,-4

NOTE: If there are multiple correct answers, return the sequence which occurs first in the array.

# HINTS
This is a very diffcult problem solving question. There has to be a few hints from the interviewer to help you here. So I will try to simulate that.
Take the example above. I assume you are able to get the N^3 runtime solution. If you haven't, figure out the brute force first before reading further. 

Your brute force solution should be taking each element then adding it, first start with subarrays of one then two, then three, etc..
Eventually, for each element you are adding increasing amount of subarrays. 1, 1+2, 1+2+-2, 1+2+-2+4, 1+2+-2+4+-4, then 2, 2+-2, 2+-2+4, 2+-2+4+-4 and so on.
Each summation is n^2 runtime and it must be done for each element so thats n^2 * n = n^3 runtime. n is the amount of elements in array.

To help you get the optimzied solution, instead ask yourself, how would you solve the question if it was instead asking find two elements that sum to zero. Then how about three elements, four??

If that didn't help, try asking yourself, how does summing two numbers get zero??

If you know one number, then the other number has to be negative or subtracted from your known number inorder to zero out.

Taking all these questions in mind, say you started at the first element, then added the second element, then third etc..
So your first pass thru, you have the summnations of each sequence starting at the first element. Can we use this to help us?
"""


def max_len_sum_zero(input_array: list[int]) -> int:
    none_zero_sums: dict[int, int] = {}
    max_length = 0
    sum = 0
    for i in range(len(input_array)):
        sum += input_array[i]
        none_zero_sums[sum] = i
        # In a case that sum == 0, the longest subarray with zero sum is
        # the entire array. The second case is when a nun zero sum
        # appears twice. In that case, the difference array has a zero
        # sum.
        if sum == 0:
            max_length = i + 1
        elif sum in none_zero_sums.keys():
            length_of_diff_array = (i + 1) - none_zero_sums[sum]
            max_length = max(max_length, length_of_diff_array)
        else:
            # We save the start of the none zero sum array.
            none_zero_sums[sum] = i
    return max_length


def main() -> None:
    array = [1, 2, 3, -6, 1, 7, 0, 0, 0, 1, -1]
    print(max_len_sum_zero(array))


if __name__ == "__main__":
    main()
