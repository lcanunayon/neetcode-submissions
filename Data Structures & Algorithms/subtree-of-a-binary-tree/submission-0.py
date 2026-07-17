"""
UNDERSTAND: Find if subroot is in the root tree
I: 2 trees root and subRoot
O: Boolean
E: Empty subroot -> true, empty root -> false, same subroot and root -> true

MATCH: DFS

PLAN: First get the subroot and run DFS. Then root for each node, find its adj 2 nodes below it. 

If the 2 nodes and the root node is the same as what was found in the subroot tree
return true, else return False

  1         1
  /\        /\ 
  3 4       4 5

False!

Eval: O(N) time O(N) space
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if not subRoot: return True
        
        if self.sameTree(subRoot, root):
          return True

        return (self.isSubtree(root.left, subRoot) or 
        self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                   self.sameTree(root.right, subRoot.right))
        return False
       