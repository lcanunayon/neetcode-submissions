"""
UNDERSTAND: The longest path between 2 nodes in the tree, does not have to be root.
I: Binary tree
O: Int rep. length of longest path in tree (diameter)
E: Empty tree -> return empty, 1 node -> return 0

MATCH: DFS, steps

PLAN: DFS, find max length found between 2 points

[1,2,4] = 2 edges

[1,2,3,5] = 3 edges

if not root:
    return (base case)

count0 = 1 + diameterOfBinaryTree(root.left)  
count1 = 1 + diameterOfBinaryTree(root.right)
return max(count0, count1)






"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0


        # Returns Height
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.res

        
        