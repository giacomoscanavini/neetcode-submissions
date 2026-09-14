class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Complexity Time: O(log(m)) + O(log(n)) = O(log(m * n))
        # Complexity Memory: O(1) to create a set of fixed int
        # Find row i to use
        i = 0
        l, r = 0, len(matrix) - 1
        while l <= r: 
            i = l + (r - l) // 2
            if matrix[i][0] <= target:
                if matrix[i][-1] >= target: break
                else: l = i + 1
            elif matrix[i][0] > target: 
                r = i - 1

        # Apply binary search to row i only
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[i][m] < target: 
                l = m + 1
            elif matrix[i][m] > target: 
                r = m - 1
            else: return True
        return False