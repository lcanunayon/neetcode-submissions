"""
UNDERSTAND: Return all UNIQUE combinations of candidates where numbers sum to target, cant choose from same number in candidate
I: Candidates int array, target int
O: List of int lists, rep. unique int combinations
E: empty candidates -> empty list, no combinations -> empty list

MATCH: Backtracking tree 

PLAN: [1,2,3,4,5] target: 7

  1             2                  5
  /   \         / \                 \  
 1,2   1      2,1  2                 5
      / \         / \                /
     1,3 1      2,3   2           *5,2
    /                /\
1,3,4               2,4 2
                        /\       
                    *2,5   2
                       
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return
            
            # include candidates[i]
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            
            # skip candidates[i]
            # [1, 1, 1, 1, 2]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        
        return res