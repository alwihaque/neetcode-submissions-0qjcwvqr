class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def is_valid_row(row: int, col: int) -> bool:
            num = board[row][col]
            for i in range(0, 9):
                if board[i][col] == num and row != i:
                    return False
            return True
        
        def is_valid_col(row: int, col: int) -> bool:
            num = board[row][col]
            for i in range(0,9):
                if board[row][i] == num and col != i:
                    return False
            return True
        
        def is_valid_box(row: int, col: int) -> bool:
            num = board[row][col]
            starting_row = (row // 3) * 3
            starting_col = (col // 3) * 3

            for i in range(starting_row, starting_row + 3):
                for j in range(starting_col, starting_col + 3):
                    if row != i and col != j and board[i][j] == num:
                        print(row)
                        print(i)
                        print(j)
                        print(col)
                        print(starting_row)
                        print(starting_col)
                        print(num)
                        return False
            return True

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    if not is_valid_row(i,j) or not is_valid_col(i,j) or not is_valid_box(i,j):
                        return False
        return True            

        