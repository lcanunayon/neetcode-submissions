"""

UNDERSTAND: Create lists in a list of nodes at each level of a binary tree  
I: Tree
O: List of lists containing nodes at each level, left to right
E: No subtree for one side -> get the other side as a list still

MATCH: BFS 

PLAN: Use BFS starting from the root to build each list, at each level to find the other nodes and build the list

BFS is a queue
1 (pop 1 get subnodes)
2, 3 (pop 2)
3, 4, 5 (pop 3)
4,5, 6, 7 (entire list)




"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        bfs = deque([root])
        #print(bfs)
        lst = []
        while bfs:
            num = bfs.popleft()
            
            bfs.append(num.left)
            bfs.append(num.right)
            lst.append([num])
        return lst


        1 (pop 1 get subnodes)
        2, 3 (pop 2)
        3, 4, 5 (pop 3)
        4,5, 6, 7 (entire list)
        """
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            level = []
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
            
















