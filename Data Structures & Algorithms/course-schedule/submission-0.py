"""
UNDERSTAND: Return a boolean if possible to finish all courses in the array. 
I: An array and an int, rep. number of courses required to take
O: Boolean value
E: Empty class -> return true, 
C: All prerequisite pairs are unique.

MATCH: Topological sort, DFS

PLAN: Use topological sort to see if all prerequisites come before each other in a logical manner

If it does, return true, if not then return false.

ex.
prereq = [[0,1],[1,0]] 

False, because 1 comes before 0, but in the second list 0 comes before 1. How can this be? It is impossible.
            1 -> 0           !=            0 -> 1

ex2. 
prereq = [0, 1]
        1 -> 0

True, because 1 comes before 0. This is the only list and it is topologically sorted, so true.

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # visitSet = all courses along the curr DFS path 
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

        # 1 -> 2
        # 3 -> 4






