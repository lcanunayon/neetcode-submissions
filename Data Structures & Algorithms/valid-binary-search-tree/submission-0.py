"""
UNDERSTAND: See if it is a valid binary search tree by seeing if the left sub is always less than node key and right sub is always greaber tha nodes key
I: Tree
O: Boolean
E: empty tree -> return True, 

MATCH: DFS

PLAN: Use DFS to check if every left side of a node is less than key
Do the same thing for the right side and check if it is greater than

Go through all nodes and check these things using DFS for the left side and the right side for all

brute force:
if not root:
    return none
if root.left:
    if root.left.val > root.val:
        return False
if root.right:
    if root.right.val < root.val:
        return False
return true
    

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True
            
            if not ( node.val < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))