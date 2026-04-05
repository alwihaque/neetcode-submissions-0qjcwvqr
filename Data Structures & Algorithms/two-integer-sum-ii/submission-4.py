class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i, j = 0, len(numbers) - 1

        while i < j: 
            
            sum_val = numbers[i] + numbers[j]

            if sum_val < target:
                i += 1

            elif sum_val > target:
                j -= 1
            
            else:
                return [i + 1, j + 1]
        

        