"""
UNDERSTAND: Find all cells were water can flow from that cell onto both oceans
I: Graph grid
O: 2d list
E: All squares not able to pass water -> return empty list

MATCH: BFS 

PLAN: Check each square and its adjacent squares to see if they are equal to or less than each other. If some squares are found,
that have this property, return the first square.  


"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
               r < 0 or c < 0 or r == ROWS or c == COLS or
               heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and  (r, c) in atl:
                    res.append([r, c])
        return res 
    