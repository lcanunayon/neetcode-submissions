class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = dict()
        tlist = dict()
        for ch in s:
            if ch not in slist:
                slist[ch] = 1
            else:
                slist[ch] += 1
        for ch in t:
            if ch not in tlist:
                tlist[ch] = 1
            else:
                tlist[ch] += 1    
        if slist == tlist:
            return True
        else:
            return False