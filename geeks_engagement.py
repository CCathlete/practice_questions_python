class Solution:
    def findTheRing(self, n: int, q: int
                    , arr: list[int], que:list[(int,int,int)]) -> list[int]:
        '''
        For each query tuple (l,r,k), 0<=l<=r<=N.
        '''
        list_of_answers = []
        for j in range(q):
            (l,r,k) = que[j]
            num = r-l-k
            if num in arr[l:int(l+(r-l)/2)]:
                num_is_in = 1
            else:
                num_is_in = 1 if num in arr[int(l+(r-l)/2):r+1] else 0
            list_of_answers += [num_is_in]
        return list_of_answers
        
        
if __name__ == "__main__":
    sol = Solution()
    N = 84
    Q = 4
    que = [(6,84,64), (19,78,2), (28,39,-8), (16,43,38)]
    arr = "0 -16 17 7 9 14 3 -14 14 -8 14 -1 1 -9 -19 -9 15 -17 -3 6" \
        + "16 16 5 -20 19 -13 8 -11 -19 -16 -13 15 -11 2 -7 3 -20 -4 17"\
        + " 16 8 -7 -1 -14 3 -14 -12 2 -13 -18 -3 8 15 -4 -8 -20 1 12 2 16 "\
        + "-2 17 -13 -11 15 -19 7 -19 8 -7 -18 -7 -16 -19 8 1 6 -15 5 12 -10 18 5 -3 -4"
    arr = arr.split(" ")
    for i in range(N):
        arr[i]=int(arr[i])     
    answer = sol.findTheRing(N, Q, arr, que)
    print(answer)