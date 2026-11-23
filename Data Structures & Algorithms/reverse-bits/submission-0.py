"""
UNDERSTAND: Reverse bits of binary of n return result
I: Binary rep. 
O: Binary rep.
E: All zeros -> return same, all ones -> return same

MATCH: Binary problem

PLAN: 
res = 0

EVAL = O(1) time and space

"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res