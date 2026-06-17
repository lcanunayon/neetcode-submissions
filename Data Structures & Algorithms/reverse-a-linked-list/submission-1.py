# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Understand: 
#Input : Single linked list
#Output: Reversed linked list, return beginning
#Edge case: No nodes -> return nothing

#Match : Change next

# Plan:
# Travel up to the last number, change its next, then change all of the nexts one by one. Also, make the last number = start

#Implement

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prev = None
        dum = head
        ahead = head.next
        while dum.next != None:
            dum.next = prev
            prev = dum
            dum = ahead
            ahead = ahead.next
        dum.next = prev
        head = dum
        return head
            
        
