# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#UNDERSTAND:
#Remove nth node from a linked list and return head
#Input: Linked list of nodes, int
#Output: Linked List

#MATCH: Double pass

#PLAN: Make the dummy head go n-1 so it can be behind the element to be removed, then change next to one after it.
# Return head afterwards

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        #print(length)
        where = length - n
        
        
        if where == 0:
            return head.next

        dummy1 = head
        for i in range(where-1):
            dummy1 = dummy1.next
        
        
        dummy1.next = dummy1.next.next
        
        return head
        

            