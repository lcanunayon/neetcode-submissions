"""
UNDERSTAND: Return with a number how many times a string containing digits can be decoded
I: String
O: Int number
E: Empty string -> returns 0

MATCH: 1d dynamic programming

PLAN: 
base case:
if i > len(s) - 1:
    return 1

dfs()



"""


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or
                s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res
        
        return dfs(0)

        

        

