class Solution:
    def wordBreak(self, s: str, wordDict: List[str], hm=None) -> bool:
        if hm is None:
            hm = {}
        if s in hm:
            return hm[s]
        if s == "":
            hm[s] = True
            return True
        
        for word in wordDict:
            
            if s[:len(word)] == word:
                if self.wordBreak(s[len(word):], wordDict, hm):
                    hm[s] = True
                    return True
        
        hm[s] = False
        return hm[s]