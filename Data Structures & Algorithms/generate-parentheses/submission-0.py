"""
UNDERSTAND: Return all types of parentheses that you can generate with n pairs of parentheses
I: integer
O: List of well-formed parentheses strings
E: int is 0 -> return empty list

MATCH: Backtrack algorithm

PLAN: 3
     /  \
  ((())) ()()
     




"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open paranthesis if open < n
        # only add a closing paranthesis if closed < open
        # valid IIF open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0,0)
        return res
