"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
UNDERSTAND: We have to copy the list, with all of the .next and .random pointers copied as well
INPUT: Linked list with a random pointer for all nodes
OUTPUT: New list with the exact properties
EDGE CASES: Empty list -> return empty, null case -> end algorithm

MATCH: Two pass, first to get length then to check nodes and properties to copy

PLAN: Get the length of linked list, to know how many nodes to create
[3,7,4,5,null] - length of 4, will create 4 new nodes with values

While doing this, there will be another node finding the next values

Have another pass to check each random, then go back to the next node with another
dummy pointer


"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur = head
        #length = 0
        #bak = None
        new_map = {}
        #pass 1: create all new nodes, map old node -> new node
        while cur:
            new_node = Node(cur.val)
            new_map[cur] = new_node
            cur = cur.next
        cur = head
        # pass 2
        while cur:
            new_map[cur].next = new_map.get(cur.next)
            new_map[cur].random = new_map.get(cur.random)
            cur = cur.next
        return new_map[head]
            
            
            
        
            
            





