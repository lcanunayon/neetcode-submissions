"""
UNDERSTAND: Return all possible subsets of nums, given an array of unique ints
I: Array nums of unique ints
O: Nested list of subsets
E: Empty nums array -> return empty subset, 

MATCH: Nested loop

PLAN: Make a nested loop over the arrays, so we can get each number in the array and see if it is part of a subset list that we create, if not then
we add to that subset list. At the end we return the subset list. 

[1,2 ,3]




"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res