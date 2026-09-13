class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find row i to use
        nrows = len(matrix)
        toprow, botrow = 0, nrows - 1
        while toprow <= botrow:
            i = (toprow + botrow) // 2
            if matrix[i][-1] < target: toprow = i + 1
            elif matrix[i][0] > target: botrow = i - 1
            else: break

        if not (toprow <= botrow): return False
        i = (toprow + botrow) // 2

        # Apply binary search to row i only
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[i][m] < target: l = m + 1
            elif matrix[i][m] > target: r = m - 1
            else: return True
        return False