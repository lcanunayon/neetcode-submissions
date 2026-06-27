# Understand: 
# Input:  Array of ints representing temperatures on the ith day
# Output : Array of ints representing number of days after ith day before warmer temperature appears.
# Edge cases: Empty temp, return empty array

# Match: Stack, list

# Plan: Put all elements into stack then count from backwards. First pop which is the rightmost of the array will be 0 because it is the end, then
#  for all subsequent checks, check if the number is less than the number just popped. If it is, we found the number of days until a higher temp. 
# [28, 40, 35, 36, 30, 38, 30]
#  0   1   2    3   4   5   6    

# for i in range(0, len(temperatures))
#       add temperature[i] to stack
#       for j in range(i+1, len(temperatures))
#           if temperature[j] > temperature[i]:
#               count = 0 


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#        seen = []
#        for i in range(0, len(temperatures)):
#            seen.append(temperature[i])
#            for j in range (i+1, len(temperatures)):
#                if temperature[j] > temperature[i]:
#                    seen.pop()
        seen = [] #pair: [temp, index]
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while seen and t > seen[-1][0]:
                stackT, stackInd = seen.pop()
                result[stackInd] = (i - stackInd)
            seen.append([t, i])
        return result

