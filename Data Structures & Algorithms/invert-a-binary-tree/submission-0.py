"""
UNDERSTAND: Invert binary tree, left subtree becomes right, right subtree becomes left
I: Tree, with root
O: Tree, with root, subtrees inverted
E: Empty tree -> return empty, only one node -> return that node

MATCH: Loop over nodes

PLAN: Recursive approach, going into each node and inverting its subtree, starting from the root, going down left and right

if root == None, return (base case)

self.left, self.right = self.right, self.left
invertTree(self.left)
invertTree(self.right)




"""

# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = root
        if dummy == None:
            return None

        dummy.left, dummy.right = dummy.right, dummy.left
        self.invertTree(dummy.left)
        self.invertTree(dummy.right)
        return root

