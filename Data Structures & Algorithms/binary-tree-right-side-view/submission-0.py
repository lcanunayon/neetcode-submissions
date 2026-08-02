"""
UNDERSTAND: Return values of nodes visible from right side of tree
I: Tree
O: List of ints rep. node vals
E: Empty tree -> return [], only root -> RETURN just root

MATCH: BFS traversal

PLAN: Start at root and add val to list with BFS 
If len(queue) == 2 -> append index 1

If len(queue) == 1 -> append that value

Do this for every level in tree until queue is not


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        res = []
        
        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightSide:
                res.append(rightSide.val)
        return res







