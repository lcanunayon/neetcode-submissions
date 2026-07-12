"""
UNDERSTAND: Data structure that can store multiple values for the same key, at dif. time stamps
I: set() -> sets a key value data structure that stores values at different time stamps, can have same key dif values
O: get() -> get a specific key value at a certain time stamp and return that keys value
E: Empty get -> return -1, 

MATCH: Dictionary

PLAN: Initialize data structure to hold keys and their values, at a certain time. We can use a dictionary, or possibly an array
{"alice" : ["happy", 1], "John" : ["sad", 2]}

"""

class TimeMap:

    def __init__(self):
        self.store = {} # key=string, value=[list of [val, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
      


    def get(self, key: str, timestamp: int) -> str:
        res = "" # holding result, return this if not found
        values = self.store.get(key, [])
        
        #binary search
        l = 0
        r = len(values)-1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp: #if under timestamp, we still return, because its the closest we found
                res = values[m][0]
                l = m + 1
            else: #invalid timestamp
                r = m - 1

        return res #final values
        


