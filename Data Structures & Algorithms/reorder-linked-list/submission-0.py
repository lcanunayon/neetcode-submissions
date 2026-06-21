# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Understand:
# Input: Ordered  Singly Linked list
# Output: Reordered linked list in the order length = n [0, n-1, 1, n-2, 2, n-3, 3, ...]
# Edge Cases: Empty List: Return None

#Match: Linked list , stack (reverse 2nd half)

#Plan: Change the next values iterating through every element in linked list.
# Two pointers for end and start, converging in
# Once they pass, terminate and give linked list back
# Make start pointer next go to the last, then move start pointer forward, repeat but opposite for the last. Repeat till low > high

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
#        if (head == None):
#            return None
#        
#        l1 = head
#        fast = head
#        l2 = head
#        remove = None
#        while(fast.next != None and fast.next.next != None):
#            fast = fast.next.next
#            remove = l2
#            l2 = l2.next#
#
#        remove.next = None
#        slowl2 = l2
#        fastl2 = l2
#        fasterl2 = l2
#        while(l2.next != None):
#            l2 = l2.next
#        while(fastl2.next != None and l2.next.next != None):
#            fastl2 = fastl2.next
#            fasterl2 = fastl2.next
#            fastl2.next 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


        




        