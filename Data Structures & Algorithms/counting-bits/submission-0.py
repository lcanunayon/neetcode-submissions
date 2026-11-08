"""
UNDERSTAND: Count number of ones in binary rep. of numbers from range [0, n]
I: N int
O: List of ints, representing number of 1's in each number
E: no edge cases

MATCH: Binary representation

PLAN: 

EVAL: O(N)

"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp