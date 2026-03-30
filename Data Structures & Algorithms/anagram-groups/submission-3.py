class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        hm = {}

        for s in strs:
            count = [0] * 26
            
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            
            if tuple(count) in hm:
                hm[tuple(count)].append(s)
            
            else:
                hm[tuple(count)] = [s]
            
        
        return list(hm.values())



        