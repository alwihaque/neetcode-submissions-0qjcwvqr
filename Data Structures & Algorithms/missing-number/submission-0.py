class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = 0
        for i in range(len(nums) + 1):
            sum1 += i
        sum2 = 0
        print(sum1)
        for n in nums:
            sum2 += n
        
        return sum1 - sum2

