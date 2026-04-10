class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for s in s1:
            count_s1[ord(s) - ord('a')] += 1
        
        l = 0
        r = l

        for r in range(len(s2)):
            count_s2[ord(s2[r]) - ord('a')] += 1

            if count_s2 == count_s1:
                return True
            
            while (r - l) + 1 > len(s1) and (s2[l] not in s1 or count_s1[ord(s2[l]) - ord('a')] != count_s2[ord(s2[l]) - ord('a')]):
                print("here")
                print(l)
                print(r)
                count_s2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if count_s2 == count_s1:
                return True
        return False
        