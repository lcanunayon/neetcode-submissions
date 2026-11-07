"""
UNDERSTAND: Return the number of 1 bits in an unsigned integer binary representation
I: Int n
O: Int rep. number of 1 bits
E: no edge case

MATCH: Bitwise operator

PLAN: Get the binary representation of n, then have a counter for all 1 bits in the binary representation

EVAL: O(32) -> O(1)

"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        #FASTER WAY
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count
        
        """
        #SLOWER WAY
        count = 0
        while n:
            count += n % 2
            n = n >> 1
        return count
        
        #1st ATTEMPT
        count = 0
        for i in range(0, 31):
            #1 << i
            if i & n:
                count += 1
        return count
        """