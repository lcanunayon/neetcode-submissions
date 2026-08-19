"""
UNDERSTAND: Have to modify land values to display number of tiles away from closest chest if reachable, if not then keep inf
I: 2D Grid
O: 2D Grid with land values modified to closest treasure chest
E: Cannot reach treasure -> land stays inf, empty grid -> return empty grid back

MATCH: BFS 

PLAN: Use BFS to find every node and calculate when we find a treasure chest how many iterations it took.

  [0,-1],
  [2147483647,2147483647]

    def islandsAndTreasure:
        r,c = len(grid), grid[0]


"""

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r,c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                (r,c) in visit or grid[r][c] == -1):
                return
            visit.add((r,c))
            q.append([r,c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
            
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            
            dist += 1