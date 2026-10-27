class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time complexity: Loop over temperatures and stack up to O(n)
        # Space complexity: Create result and stack arrays O(n)
        result = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while len(stack) > 0 and t > stack[-1][0]:
                stackTemp, stackIdx = stack.pop(-1)
                result[stackIdx] = i - stackIdx

            stack.append((t, i))

        return result
            