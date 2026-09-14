class Solution:
    def climbStairs(self, n: int) -> int:
        # Complexity Time: O(n)
        # Complexity Memory: O(1)
        oneStepAway, twoStepAway = 1, 1
        # twoStepAway becomes oneStepAway
        # oneStepAway sums the previous two steps as we climb
        for i in range(n - 1):
            twoStepAway, oneStepAway = oneStepAway, oneStepAway + twoStepAway
        return oneStepAway

        


        