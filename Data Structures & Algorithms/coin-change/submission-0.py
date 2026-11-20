"""
UNDERSTAND: Return fewest amount of coins to reach amount
I: Int array coins, int amount
O: Int 
E: Cant get exact amount -> return -1

MATCH: 1d Dynamic problem

PLAN: coins = [1,5,10], amount = 12

base case:
    sum >= amount -> return 0

memoization (use a dictionary cache to record result for each recur. call)
return from cache instead of recalculating
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1