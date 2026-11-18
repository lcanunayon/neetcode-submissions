"""
UNDERSTAND: Find subarray with the largest sum, then return its sum
I: nums int array
O: Int rep. largest sum
E: no edge cases

MATCH: Greedy

PLAN:
 
brute force:

running sum = 0
for i in range(1 loop):
    sum = i
    for j in range(2nd loop):
        sum += j
    
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub