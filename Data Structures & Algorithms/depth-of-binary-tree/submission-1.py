"""
UNDERSTAND: Return the height of the tree, i.e. its longest path down
I: Tree
O: Int rep. height of tree
E: One node -> return 1, empty tree -> return none, 

MATCH: Depth first search

PLAN: Recursive

We can keep a step count every time we go down a node, do this for each path

Find the max step count for all paths, that is the height

(self, root, count)

if root == None:
    (base case)

if max(height, count) == count -> height = count

loop through

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        