class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count_t, window = {}, {}

        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)
        

        have, need = 0, len(count_t)

        min_window, min_l = [-1, -1], float('inf')

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < min_l:
                    min_window = [l , r]
                    min_l = (r - l) + 1
                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                
                l += 1
        
        if min_window == [-1, -1]:
            return ""
        
        return s[min_window[0]: min_window[1]+1]

        
        