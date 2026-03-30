class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = {}

        for i in range(0, len(s)):
            if s[i] not in hm:
                hm[s[i]] = 1
            else:
                hm[s[i]] += 1
        
        for i in range(0, len(t)):
            if t[i] in hm:
                hm[t[i]] -= 1
            else:
                hm[t[i]] = 1

        for value in hm.values():
            if value != 0:
                return False
        return True