"""
UNDERSTAND: Make a cache class with a init, then get and put methods. If putting a new int exceeds capacity, remove least recently used key
INPUT: put(): takes a key and value, and adds to the cache
OUTPUT: get(): returns value from key which it was called on, doesnt remove
EDGE CASE: put() into a list too big -> remove least used key, 

MATCH: Dictionary, linked list

PLAN: Init class, use a linked list to put items

"""

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None   
        self.next = None 


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #map key to nodes

        # left = LRU, right = most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left


    #remove node from list (HELPER)
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    #insert at right (HELPER)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1    
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        #does len of cache exceed cap?
        if len(self.cache) > self.cap:
            #remove from the list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]    
        
        
        
