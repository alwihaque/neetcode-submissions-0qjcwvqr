class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        outer_left, outer_right = 0, len(matrix) - 1

        while outer_left <= outer_right:
            outer_m = outer_left + (outer_right - outer_left) // 2

            row = matrix[outer_m]
            print(row)
            
            if target < row[0]:
                outer_right = outer_m - 1
            
            elif target > row[len(row) - 1]:
                outer_left = outer_m + 1
            
            else:
                l, r = 0, len(row) - 1
                

                while l <= r:
                    m = l + (r - l) // 2

                    if target < row[m]:
                        r = m - 1
                    elif target > row[m]:
                        l = m + 1
                    else:
                        return True
                    
                return False
            

        return False 
        