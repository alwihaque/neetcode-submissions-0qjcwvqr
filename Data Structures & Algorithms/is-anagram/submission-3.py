class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hm = {}

        for ch in s:
            if ch in hm:
                hm[ch] = hm.get(ch) + 1
            else:
                hm[ch] = 1

        for ch in t:
            if ch in hm:
                hm[ch] = hm.get(ch) - 1

            else:
                hm[ch] = 1

        for key in hm.keys():
            if hm[key] > 0:
                return False

        return True    


        