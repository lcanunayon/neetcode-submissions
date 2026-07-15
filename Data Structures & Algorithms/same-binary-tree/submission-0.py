"""
UNDERSTAND: Return true if 2 trees are equivalent, return false otherwise
I: 2 tree objects
O: Boolean
E: Empty trees -> true, one empty -> false

MATCH: BFS

PLAN: we are to check if each new visited node is the same for both trees

1 -> 2, 3 (one list)
== they are equivalent
1 -> 2, 3 (second list)

4 -> 7 (left), null (right)

!= not equivalent

4 -> null (left), 7 (right)

BFS -> queue, when gotten from queue pop the node we are going to, and append its neighbors

nested function for bfs to hold

EVAL: O(N^2)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
        """
        if not p and not q: #both empty edge case
            return True        
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))




        