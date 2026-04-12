class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res, parenthesis = [], []

        openN, closedN = 0, 0

        def backtrack(openN, closedN):
            if openN == closedN == n:
                par = "".join(parenthesis)
                res.append(par)
                return
            
            if openN < n:
                parenthesis.append('(')
                backtrack(openN + 1, closedN)
                parenthesis.pop()
            
            if closedN < openN:
                parenthesis.append(')')
                backtrack(openN , closedN + 1)
                parenthesis.pop()
        
        backtrack(0,0)
        return res


                
        