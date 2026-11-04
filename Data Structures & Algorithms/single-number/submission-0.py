"""
UNDERSTAND: Return the integer appearing once in a list array
I: List of ints
O: Int
E: Empty list -> return nothing

MATCH: Dictionary

PLAN: Use a hash set to find the frequencies of each number, return the number with a freq of 1

IMPLEMENT:


"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # n ^ 0 = n
        for n in nums:
            res = n ^ res
        return res

        
        """
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        for key in freq:
            #print(key)
            if key == 1:
                return key
        return -1
        """