class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        charset = set()
        max_l = 0
        for r in range(len(s)):
            
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            max_l = max(max_l, r - l + 1)
        return max_l    



        