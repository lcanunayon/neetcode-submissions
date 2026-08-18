"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
UNDERSTAND: Create a copy of the graph
I: Adjacency list
O: Exact same adjacency list
E: Empty graph -> return empty list, one node -> return a list of an empty list

MATCH: DFS , return nested loop (if not empty)

PLAN: Go through each node, building the nested list by checking
each node and its neighbors, adding those neighbors as lists into
the full list

def clone:
    cloneList = []
    cloneList.append()
 


"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None

