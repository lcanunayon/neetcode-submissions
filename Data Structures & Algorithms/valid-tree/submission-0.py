"""
UNDERSTAND: Check whether undirected edges make a valid tree
I: int n, edge graph
O: boolean val
E: Empty edges -> return false

MATCH: cycle checking programing (dfs)

PLAN: make dfs function for checking a cycle, using edge set

cycle = {}
def dfs(root):
if root == None:
    return

if root not in cycle:
    cycle.add(root)
else:
    return false
return true


"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = {i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visit)


        """
        cycle = {}

        def dfs(edges):
            for edge in edges:
                if edge == None:
                    return
                
                if edge[0] not in cycle:
                    cycle[edge] = (edge[0:1])
                    dfs(edge)
                else:
                    return False
            return True
        return dfs(edges)
        """
        
        

