class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch = ""
        for s in s:
            if s.isalnum():
                ch += s
        #print(ch)
        lo = 0
        hi = -1
        for c in ch:
            
            if ch[lo].lower() != ch[hi].lower():
                return False
            lo += 1
            hi -= 1
        return True