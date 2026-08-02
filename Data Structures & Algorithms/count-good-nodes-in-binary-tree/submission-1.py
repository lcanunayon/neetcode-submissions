"""
UNDERSTAND: Return number of good nodes, nodes where a path from that node
to that node contains no value greater than that node. 
I: Tree
O: Int 
E: Empty tree -> return 0

MATCH: BFS  

PLAN: Check if any values at any level bigger than root val, it is a 
good node.

If the node.val we popped is bigger than the root, count it as a good node


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, root.val)

                
                










