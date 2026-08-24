"""
UNDERSTAND: Return the k closest points to the (0,0 origin)
I: List[List[ints]] representing points on a graph
O: List[List[ints]] closest k points
E: Empty points -> empty return list, same 2 points -> return first one in list

MATCH: Min heap

PLAN: Use min heap to find the smallest in heap, then return that point

[[0,2], [2,2]]

pq ->

(eulicid eq. on [0,2]) = 2 -> this is the smallest, this is the closest point, pop from heap

(eulicid eq. on [2,2]) = 2.8 

since k = 1 in this test, we return only [[0, 2]]

"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap) #turn list into heap
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        
        return res