"""
UNDERSTAND: Car fleet is a group of cars going the same pos and speed, 1 car is a fleet. Return number of different fleets that arrive at dest.
I: Target int for finish, int[] pos array, int[] speed array
O: Int representing number of different car fleets that arrive at destination
E: No car fleet reaches -> return 0,

MATCH: Stack

PLAN: target = 10, position = [1,4], speed = [3,2]
each i is a car

     3     2
pos [1,2,3,4,5,6,7,8,9,10]

 target = 10, position = [4,1,0,7], speed = [2,2,1,1]

     1 2     2     1
pos [0,1,2,3,4,5,6,7,8,9,10]

each car has to hit the finish, see how many fleets after cars journey, time based

when you pop from stack, theres one less fleet, if each number in stack rep. a fleet

we can have each car rep. in stack, let it do its thing, if their positions ever equal each other, pop from stack since 2 fleets became one.
Count how many is left in stack at the end when every car reached target

(pos) -> if pos >= target, stop iterating on it

loop an addition for speed, starting value being the position
pos 1
speed 3 = 4 + 3 = 7 + 3 = 10 .. hit target!

[step, step]
  5     2      2
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]: #Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        
                            
        

        