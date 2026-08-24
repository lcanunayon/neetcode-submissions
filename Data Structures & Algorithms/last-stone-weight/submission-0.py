"""
UNDERSTAND: Find the sum of all the stones when every 2 are smashed together, in a conversion 
I: Array of stones  
O: Integer of what is left
E: All destroy each other -> return 0, empty stones list -> return 0

MATCH:  Priority queue, find 2 heaviest every time                                                                                      

PLAN: Use priority queue for heaviest 2, which ever one is heavier, subtract the smaller from heavier and remove smaller from list

If it is the same, remove both from list

[2, 3, 6, 2, 4] -> [6,4,3,2,2] PQ

pass 1: 6 and 4, 6 > 4, 6 - 4 = 2, delete 4 and change 6 to 2

[2,3, 2, 2] -> [3,2,2,2] PQ

pass 2: 3 and 2, 3 > 2, 3 - 2 = 1, delete 2 and change 3 to 1

[2, 1, 2] -> [2,2,1] PQ

pass 3: 2 and 2, 2 == 2, remove both

[1] is the final answer

        pq = []
        pq.append(stones.pop(max(stones)))
        while pq:
            pq.append(stones.pop(max(stones)))
            if pq[0] > pq[1]:
                stones.append(pq.pop(pq[0]) - pq.pop(pq[1]))
            elif pq[0] < pq[1]:
                stones.append(pq.pop(pq[1]) - pq.pop(pq[0]))
            else:
                pq.pop(pq[0])
                pq.pop(pq[1])
        return stones
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])











        