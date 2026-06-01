class Solution:
    def isValidSudoku(self, board):
        # Brute force 
        rows = [[] for _ in range(len(board))]
        cols = [[] for _ in range(len(board))]
        boxs = [[] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == '.': continue
                else:

                    if 0 <= i <= 2:
                        if 0 <= j <= 2: k = 0
                        elif 3 <= j <= 5: k = 1
                        else: k = 2
                    elif 3 <= i <= 5:
                        if 0 <= j <= 2: k = 3
                        elif 3 <= j <= 5: k = 4
                        else: k = 5
                    else:
                        if 0 <= j <= 2: k = 6
                        elif 3 <= j <= 5: k = 7
                        else: k = 8

                    print(f"Considering: {num} in row {i} and col {j} and box {k}")

                    if num in rows[i]: return False
                    else: rows[i].append(num)

                    if num in cols[j]: return False
                    else: cols[j].append(num)

                    if num in boxs[k]: return False
                    else: boxs[k].append(num)
        return True