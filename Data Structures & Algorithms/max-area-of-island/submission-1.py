"""
UNDERSTAND: The biggest island of 1's, connected horizontally or vertically, and then return its area
I: Graph 
O: Int rep. the biggest islands area
E: All 0's -> return 0, on a diagonal -> own separate islands

MATCH: BFS to find 1's, and then parse to see its size

PLAN: Use BFS to find 1's in the graph, when found one then look for more vertically and horizontally, and increment a count



"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                grid[r][c] == 0 or (r,c) in visit):
                return 0
        
            visit.add((r, c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area  



