"""
UNDERSTAND: Return number of substrings in s that are palindromes
I: string s
O: Int
E: empty string -> return 0

MATCH: 1d dynamic programming

PLAN: "aaa"

3 one letter palindromes:
a a a

2 two letter:
aa aa

1 three letter:
aaa

for i in range(len(s)):
    if s[i] == s[i+1] and s[i] == s[i-1]:
        increment count
    if s[i] == s[i+1]:
        increment count
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
        """
        MY WAY
        count = 0
        for i in range(len(s)):
            if s[i] == s[i+1] and s[i] == s[i-1]:
                count += 1
            if s[i] == s[i+1]:
                count += 1
        return count
        """