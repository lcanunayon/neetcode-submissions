#make set we add onto
# iterate through a l and r pointer, looking for new char for the set
# if char not in set, add
#if duplicate found, split off
#return the length of set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

