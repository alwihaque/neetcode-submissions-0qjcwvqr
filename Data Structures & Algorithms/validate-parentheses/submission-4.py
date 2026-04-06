class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for c in s:

            if c in pairs.values():
                stack.append(c)
            elif c in pairs.keys():
                item = stack.pop(-1) if len(stack) > 0 else ""
                if item != pairs[c]:
                    return False
        
        return len(stack) == 0
        