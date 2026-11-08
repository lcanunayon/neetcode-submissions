"""
UNDERSTAND: Return a valid ordering of courses to finish all courses
I: Int rep. number of courses, prerequisite list
O: List of valid ordering of courses
E: 0 Courses -> return empty list

MATCH: Graph

PLAN:  


"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list of prereqs
        prereq = { c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # a course has 3 possible states:
        #visited -> crs added to output
        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle
        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
            
                