# UNDERSTAND: Return minimum element of rotated array either 1 and n times. If rotated the same amount of the length of list, it becomes the same.
#Input: Int array that has been rotated
#Output : Minimum value in array
#Edge case: empty list -> return empty, rotated same length of array -> same array

#Match: Binary search, watch out for non ordered lists

#Plan : Order the list, then run binary search on it
# len 6, [1,2,3,4,5,6] -> [3,4,5,6,1,2], [2,3,4,5] , [4,5,0,1,2,3]
#
# find mid, if nums[mid] > nums[hi] -> lo = mid + 1, if nums[mid] < nums[lo] -> lo = mid
# 

#Evaluate: O( log n ) time O(1) space

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]