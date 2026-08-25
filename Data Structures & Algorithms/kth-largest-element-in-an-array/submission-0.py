"""
UNDERSTAND: Returning the kth largest element in an unsorted array
I: Unsorted array of ints
O: Int rep. kth largest element
E: Over the largest element -> return closest value, empty array -> return -1

MATCH: Priority heap, 

PLAN: Use a priority heap to keep the largest element in front, then keep popping k amount of times, until the last pop is the number we need.

Then we return that number.

def findKthlARGEST:
    heapify list
    for i in range(k-1)
        if heap:
            heapp.pop
    if heap:
        num = heapp.pop
        return num
    else:
        return -1

[2,3,1,5,4]


        heap = []
        while len(heap) < k:
            heapq.heappush(heap, max(nums))
            
        num = heapq.heappop(heap)
        return num
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k: return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else:   return nums[p]
        
        return quickSelect(0, len(nums) - 1)












