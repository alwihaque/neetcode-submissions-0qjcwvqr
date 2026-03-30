class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_count = {}

        for letter in s:
            freq_count[letter] = freq_count.get(letter, 0) + 1
        
        for letter in t:
            freq_count[letter] = freq_count.get(letter, 0) - 1

        for key in freq_count:
            if freq_count[key] != 0:
                return False
        return True
        