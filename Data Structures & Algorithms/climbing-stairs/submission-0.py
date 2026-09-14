class Solution:
    def climbStairs(self, n: int) -> int:
        # Complexity Time: O(n)
        # Complexity Memory: O(1)
        one, two = 1, 1
        for i in range(n - 1):
            two, one = one, one + two

        return one

        


        