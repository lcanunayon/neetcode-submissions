"""
UNDERSTAND: Given a # of steps to reach top of staircase, return number of distinct ways to climb staircase taking 1 or 2 steps
I: Int rep. # of steps
O: Int rep. # of distinct ways to reach top
E: Input 0 -> return 0, 

MATCH: 1d Dyanmic, cached array utilizing memoization

PLAN: Cache the return from each subproblem when using either 1 or two steps, then icrement count each time.


"""

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one