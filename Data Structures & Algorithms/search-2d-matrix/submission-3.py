class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time complexity: Binary search among rows and among columns O(logn + logm) = O(log(n*m))
        # Space complexity: Create fixed number of variables O(1)
        if target < matrix[0][0] or target > matrix[-1][-1]: return False
        
        # Find row
        r1, r2 = 0, len(matrix)
        while r1 < r2:
            m = r1 + (r2 - r1)//2
            if target < matrix[m][-1]: r2 = m
            elif target > matrix[m][-1]: r1 = m + 1
            else: return True
        row = r2
        
        # Find col within row
        c1, c2 = 0, len(matrix[row])
        while c1 < c2:
            m = c1 + (c2 - c1)//2
            if target < matrix[row][m]: c2 = m
            elif target > matrix[row][m]: c1 = m + 1
            else: return True
        
        return False