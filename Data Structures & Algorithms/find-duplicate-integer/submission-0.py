"""
UNDERSTAND: There is one duplicate number, the rest are unique
INPUT: Int array
OUTPUT: The duplicate int
EDGE CASE: Empty array -> return empty, 

MATCH: Dictionary to count freq

PLAN: Use a dictionary to map out each unique num and its frequency, then return the one that has more than 1 in dict

"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        key = [key for key, val in seen.items() if val > 1]
        return key[0]
        