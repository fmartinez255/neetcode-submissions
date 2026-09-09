class Solution:
    def __init__(self):
        self.lookup = {0: 0, 1: 1, 2: 2} # store results for 0, 1, 2

    def climbStairs(self, n: int) -> int:
        # recursive solution

        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        if n in self.lookup:
            return self.lookup[n]
        else:
            res = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.lookup[n] = res
        
        return res