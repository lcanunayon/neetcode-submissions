#Understand:
#Input: List of strings representing an arithmetic expression
#Output: Int (After evaluating expression)
#Edge: Empty list, return empty. 

#Match: Stack, list

# Plan: Add each string to a stack, keep it as an int if int, if it is a operation, we pop the last 2 things out of the stack and do that operation
#on it. This should get the reverse polish notation we are looking for.

#Implement

# Review

# Evaluate = O(N) time O(N) space

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if(len(tokens) == 0):
            return None
        
        seen = []
        for s in tokens:
            if s == "+":
                #if seen and len(seen) > 1:
                    int2 = seen.pop()
                    int1 = seen.pop()
                    val = int(int1) + int(int2)
                    seen.append(val)
            elif s == "-":
                #if seen and len(seen) > 1:
                    int2 = seen.pop()
                    int1 = seen.pop()
                    val = int(int1) - int(int2)
                    seen.append(val)
            elif s == "*":
                #if seen and len(seen) > 1:
                    int2 = seen.pop()
                    #print(int2)
                    int1 = seen.pop()
                    val = int(int1) * int(int2)
                    seen.append(val)
            elif s == "/":
                #if seen and len(seen) > 1:    
                    int2 = seen.pop()
                    int1 = seen.pop()
                    val = int(int1) / int(int2)
                    seen.append(val)
            else:
                seen.append(s)
        return int(seen.pop())