class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hm = {}

        for i, x in enumerate(s):
            hm[s[i]] = hm.get(s[i], 0) + 1
            hm[t[i]] = hm.get(t[i], 0) - 1
        
        for i in hm.values():
            if i != 0:
                return False
        
        return True
        