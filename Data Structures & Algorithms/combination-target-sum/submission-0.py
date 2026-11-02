"""
UNDERSTAND: Return all combinations of nums that sum to target
I: Nums array, target int
O: List of lists (int combinations)
E: Empty nums  -> return empty list, no combinations-> return empty list

MATCH: Backtrack tree

PLAN: 
nums = [2,5,6,9]
target = 9

   2 
    \ 
     2 (4)
      \ 
       5 (9)     

[2,5,6,9]

combinationSum(self, nums[i+1])
sum
 base case:
 if sum == target:
    sumSets.append(sum numbers)

 if sum + num <= target:
    get num
    combinationSum(self, sum)


"""

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return 
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res