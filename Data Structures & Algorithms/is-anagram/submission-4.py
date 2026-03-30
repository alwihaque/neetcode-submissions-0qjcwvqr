class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hm = {}

        for ch in s:
            hm[ch] = hm.get(ch, 0) + 1
        
        
        
        for ch in t:
            if ch in hm:
                hm[ch] -= 1
            else:
                hm[ch] = 1
        
        
        for v in hm.values():
            if v > 0:
                return False
        
        return True
        