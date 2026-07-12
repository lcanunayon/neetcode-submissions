"""
UNDERSTAND: Given 2 arrays, find the median of the 2 arrays combined, sorted in ascending. Math if 2 are the median.
I: 2 int arrays
O: single int representing median of both arrays
E: Empty list -> return empty, 2 medians -> find the average

MATCH: Binary search, array manipulation

PLAN: Merge the lists into a new list
[1,2,3,4]

[1,2,3], [4]
[1,2,3,4,5,6]
     ^ 
    bottom med
[1,2,3][4,5,6]

[1,2,3,4]
     ^
    top med
[1,5],[4,6,8]
[1,4],[5,6,8]

[1,2,3,4,5,6,7,8]

, []
[1,2], [3,4,5]

lo = 1
hi = 4

target = end
mid < 4

If even number of elements, if mid is less than  
"""
#solution

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True: #return to finish
            i = (l + r) // 2 #middle value of array A for left partition
            j = half - i - 2 # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2:
                    return min(Aright, Bright)
                #even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1



