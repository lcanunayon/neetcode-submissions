class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            total_hours = sum((p + mid - 1) // mid for p in piles)
            if total_hours <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo