# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Understand:
#In: linked list with possible cycle
#Out: Boolean (true or false)
#Edge Case: empty list: return false, unconnected nodes: ignore

# Match : Linked List, List

# Plan:
# while (node.next != null), if node not in acc[], append, if it is, return false, return true after everything checked

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head == None):
            return False
        
        
        slow = head
        fast = head
        while (slow.next != None and fast.next != None and fast.next.next != None):
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False        


        