class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count, window = {}, {}
        for i in t:
            count[i] = 1 + count.get(i,0)

        have, need = 0, len(count)

        res, res_l = [-1, -1], float("infinity") 

        l = 0

        for r in range(len(s)):
            
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in count and count[s[r]] == window[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < res_l:
                    res = [l, r]
                    res_l = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res 

        return s[l: r+1] if res_l != float("infinity") else ""