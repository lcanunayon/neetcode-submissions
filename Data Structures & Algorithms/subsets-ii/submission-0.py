"""
UNDERSTAND: Return all possible subsets of an int array nums
I: Int array
O: Array of int arrays, rep. subsets
E: Empty nums -> return single empty array, 

MATCH: Backtracking algorithm

PLAN: I: [1,2,1]

O: [[],[1],[1,2],[1,1],[1,2,1],[2]]
     
     [1,2,1] (from the whole list)
     / 
    1
    /\
   1,2 1
    /   / 
1,2,1   1,1
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return 
            
            # all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # all subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])
        return res


        """
        nums = nums.sort()
        lst = []

        def dfs(nums):
            if len(nums) == 0:
                return nums
            #[1,1,2]
            subset = self.subsetsWithDup(nums[:1])
            if subset not in lst:
                lst.append(subset)
        dfs(nums)
        return lst
        """        
