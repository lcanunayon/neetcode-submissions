"""
UNDERSTAND: Find number of connected components in graph
I: int n rep. nodes, undirected graph
O: int rep. number of CC's
E: Empty edges -> return 0

MATCH: DFS problem

PLAN: Use DFS on all unvisited nodes, count from graphs travelled

count var
unvisited set

or Start with n components and decrement depending on if nodes can be connected together

res = n


"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]] 
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res






