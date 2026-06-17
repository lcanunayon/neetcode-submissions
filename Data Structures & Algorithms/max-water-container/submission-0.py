#check each left and right height
#multiply the lower of the two
#try to accumulate the biggest amount between
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res


