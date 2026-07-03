# UNDERSTAND: Same rotated array as before, only we are searching now
#INPUT: Rotated sorted array
#OUTPUT: Integer rep. index of target or -1 if not present
#EDGE CASES: Not in list -> return -1, 

#MATCH: Binary search, changed so it looks for breakpoint in rotated array

# Plan: Compare mid to hi and target. If mid > hi and mid > target -> hi = mid - 1
# elif mid < lo and mid <target -> lo = mid + 1
# else return nums[mid]

# [3,4,5,6,1,2] target 3
# l = 0, r = 5, mid = 2 giving int 5

# 



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                #left half is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                #right half sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
        