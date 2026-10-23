class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time complexity: nested loop to scan the board O(n^2)
        # Space complexity: create 3 hash map up to O(n^2)
        rows = {}
        cols = {}
        boxs = {}
        
        nrows = len(board)
        ncols = len(board[0])

        for row in range(nrows):
            rows[row] = rows.get(row, set())
            for col in range(ncols):
                box = 3 * (row // 3) + col // 3
                cols[col] = cols.get(col, set())
                boxs[box] = boxs.get(box, set())

                if board[row][col].isdigit():
                    if (board[row][col] in rows[row] or 
                        board[row][col] in cols[col] or 
                        board[row][col] in boxs[box]):
                        return False
                    else:
                        rows[row].add(board[row][col])
                        cols[col].add(board[row][col])
                        boxs[box].add(board[row][col])

        return True