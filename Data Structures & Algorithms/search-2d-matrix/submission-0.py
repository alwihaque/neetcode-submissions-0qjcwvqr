class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # need to get row
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1

        while top <= bottom:
            m = (top + bottom) // 2

            if target > matrix[m][-1]:
                top = m + 1
            
            elif target < matrix[m][0]:
                bottom = m - 1

            else:
                break
            
        if not (top <= bottom):
            return False
        row = (top + bottom) // 2        
        left, right = 0, cols - 1

        while left <= right:
            m = (left + right)//2

            if target > matrix[row][m]:
                left = m + 1
            elif target < matrix[row][m]:
                right = m - 1
            else:
                return True
        return False
        



            
        