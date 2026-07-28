"""
UNDERSTAND: Trying to find the node in a tree that connects nodes p and q. It can also be a descendant of itself as well.
I: Binary Tree
O: One node rep. lowest common ancestor of p and q
E: Empty tree -> return None, no common ancestor -> return -1

MATCH: DFS (look at every node and its descendants, including itself)

PLAN: Use DFS to go down the whole branch of each subtree, checking each node if it has p and q, including itself. If found, return that node value.

    5
   / \ 
   3  8
  / \ / \
  1 4 7  9
   \
    2

p= 3 , q = 8

for each node:
    if node.left.val == p and node.right.val == q:
        do
    elif node.left.val == q and node.right.val == p:
        do
    elif node.val == q and node.left.val == p or node.right.val == p

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur