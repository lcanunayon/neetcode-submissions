"""
UNDERSTAND: Return the kth smallest value (1 index)
I: Tree
O: Int 
E: Empty tree -> return 0,

MATCH: DFS

PLAN: Keep a tracker for minimum at every single node in the tree. Change the minimum from "-inf" first to the next minimum for kth many times.

[2,1,3], k = 1



"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
        return -1
