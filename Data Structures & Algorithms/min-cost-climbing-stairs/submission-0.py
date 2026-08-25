"""
UNDERSTAND: Each step has a cost, you pay the cost at that step which is the value then either take 1 or 2 steps. Just past the last index is the top.
I: Cost array
O: Int rep. minimum cost to reach top
E: One step -> one cost, no costs -> return 0

MATCH: DP Program

PLAN:

count = 0
while ind < len(cost):
    if [i+1] > [i+ 2]:
        ind += 2
        count += cost[ind]
    elif [i+1] < [i + 2]:
        ind += 1
        count += cost[ind]
    else:
        ind += 2
        count += cost[ind]
return count




"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])