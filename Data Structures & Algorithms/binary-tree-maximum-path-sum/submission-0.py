"""
UNDERSTAND: Return maximum path sum in tree, may or may not include root
I: Tree 
O: Int 
E: Negative values -> skip if not largest sum

MATCH: DFS, counting sum problem

PLAN: Start from root, keep a counting variable
Check every path if counting sum is max

Calculate each subtree node all the way to its parent, in order to extend the path
Take max(0)  to avoid negative sums
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]