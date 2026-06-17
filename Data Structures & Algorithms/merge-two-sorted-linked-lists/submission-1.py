# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Understand:
# Input: 2 sorted linked lists
# Output: 1 sorted linked list made from the 2 linked lists
# Edge case: empty list -> ignore, negative numbers -> should still work with logic

# Match: Process linked list, make like zipper

#Plan:
# if (list1.val < list2.val):
# add list1 to newlist
# elif >
# add list2 to newlist
# else:
# just add list1 to newlist 

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #newlist = ListNode(None)
        prev = None
        #if list1 == None:
            #return list2
        #if list2 == None:
            #return list1
        dummy = ListNode()
        tail = dummy
        #dum2 = list2
       # ahead1 = list1.next
        #ahead2 = list2.next
        #res= list1
        while list1 and list2:
            if(list1.val <= list2.val):
                tail.next = list1
                list1 = list1.next
            #elif (dum1.val > dum2.val):
             #   dum2.next = dum1
              #  dum2 = ahead2
               # ahead2 = ahead2.next
            else:
                tail.next = list2
                list2 = list2.next
                #ahead1 = ahead1.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next
        #if (dum1.val < dum2.val):
        # dum1.next = dum2
        # dum2 = ahead1
        #  elif (dum1.val > dum2.val):
        #   dum2.next = dum1
        #     dum1 = ahead2   
        #else:
        #   dum1.next = dum2
        #  dum2 = ahead1      
        
        # return res
                