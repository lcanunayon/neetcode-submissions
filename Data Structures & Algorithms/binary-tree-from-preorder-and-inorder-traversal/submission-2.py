"""
UNDERSTAND: Rebuild the binary tree from preorder and inorder, then return root of built tree
I: preorder array traversal, inorder array traversal
O: Built tree
E: empty arrays -> return empty

MATCH: Inorder + preorder + DFS

PLAN: Split inorder array in half, then use preorder array to build tree from root down.
Or use hashmap to get node and its value



"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val: i for i, val in enumerate(inorder)}
        self.pre = 0

        def build(lo, hi):          # builds the subtree covering inorder[lo..hi]
            if lo > hi:
                return None
            val = preorder[self.pre]
            self.pre += 1
            root = TreeNode(val)
            mid = idx[val]
            root.left = build(lo, mid - 1)    # must come before right
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)
        """
        NeetCode Answer (TLE):
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
        """