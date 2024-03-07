
from typing import List


class Solution:
    """
    given a tree consisting of n nodes and (n-1) edges, where the nodes are labelled from 1 to on and the root node is 1, the objective is to determine the count of good subtrees in the tree.
    A subtree is called a good subtree if the summatino of all the node values in that subutree modulo 10**5 + 3 becomes a prime number.
    """
    def primeSumSubtrees(self, n : int, edges : List[List[int]]) -> int:
        