class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            if ch in pairs.keys():
                if len(stack) == 0:
                    return False
                elem = stack.pop()
                if elem != pairs[ch]:
                    return False
        
        return len(stack) == 0

        