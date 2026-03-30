class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        def valid_rows(board: List[List[str]]) -> bool:
            

            for i in range(9):
                seen = set()
                for j in range(9):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in seen:
                        return False
                    
                    seen.add(board[i][j])
 
            return True
        
        def valid_cols(board: List[List[str]]) -> bool:

            for j in range(9):
                seen = set()
                for i in range(9):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in seen:
                        return False    
                    seen.add(board[i][j])
            return True

        def valid_sub_boxes(board: List[List[str]]) -> bool:
            row_start = 0
            while row_start < 9:
                col_start = 0
                while col_start < 9:
                    seen = set()
                    i = row_start
                    while i < row_start + 3:
                        j = col_start
                        while j < col_start + 3:
                            if board[i][j] != '.':
                                if board[i][j] in seen:
                                    return False
                                seen.add(board[i][j])
                            j += 1
                        i += 1
                    col_start += 3
                row_start += 3
            
            return True
        
        return valid_rows(board) and valid_cols(board) and valid_sub_boxes(board)



        



                
        