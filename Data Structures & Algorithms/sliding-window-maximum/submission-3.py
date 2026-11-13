"""
UNDERSTAND: Sliding window of size k, return a function showing biggest element until it reaches the right edge
I: Int array nums, int k
O: Int array
E: Empty nums -> return empty list

MATCH: Sliding window

PLAN: 
left and right pointers at the length k


"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() #index
        l = r = 0

        while r < len(nums):
            #popping smaller element
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # remove left val from window
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]]) #the biggest element
                l += 1
            r += 1
        
        return output

        """
        too inefficient (brute force)
        l, r = 0, k
        res = []

        while r <= len(nums):
            res.append(max(nums[l:r]))
            l += 1
            r += 1
        
        return res
        """