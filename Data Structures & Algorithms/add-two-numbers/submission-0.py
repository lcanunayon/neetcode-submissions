# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
UNDERSTAND: In a linked list in reverse order, add the values and return the sum as
a backwards linked list.

INPUT: Single linked list, rep. a number in reverse
OUTPUT: Same thing, rep. the sum
EDGE CASE: 0 -> add like normal

MATCH: Loop with a carry value

PLAN: 20 + 20, use modulo to get carry value if over 10 
Calculate sum from right to left
Similar to the addition algorithm used in elementary

"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dummy = ListNode()
        res = dummy
        s = 0 
        carry = s

        while l1 or l2:
            s = carry
            
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            
            num = s % 10
            carry = s // 10
            new_node = ListNode(num)
            dummy.next = new_node
            dummy = dummy.next
        if carry:
            new_node = ListNode(carry)
            dummy.next = new_node
        return res.next








