"""
UNDERSTAND: Return true if tree is balanced (i.e. left and right subtree differ in height by no more than 1), false otherwise
I: Tree
O: Boolean
E: 1 node -> True, no node -> return None, 

MATCH: DFS, 

PLAN: Height of both subtrees, return true if abs(sub1 - sub2) < 1

Run DFS on both subtrees, getting the height for both subtrees

Nested function, getting the return values from that function and working on it
Check if only one node

   1
   /\
  2  3
     /
    4
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        #nested DFS
        def dfs(root):
            if not root:
                return 0
            
            return 1 + max(dfs(root.left), dfs(root.right))
        
        if not root:
            return True
        elif root.left and root.right:
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            return (abs(left_height- right_height) <= 1)
        elif root.left:
            return dfs(root.left) <= 1
        elif root.right:
            return dfs(root.right) <= 1
        else:
            return True
        """
        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and (abs(left[1] - right[1])) <= 1)
            
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]


        

            
            