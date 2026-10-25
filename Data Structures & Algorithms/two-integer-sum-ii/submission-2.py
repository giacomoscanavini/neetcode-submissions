class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time complexity: Loop over the numbers O(n)
        # Space complexity: Create fixed amount of variables O(1)
        i = 0
        j = len(numbers) - 1
        while i < j:
            value = numbers[i] + numbers[j]
            if value < target: i += 1
            elif value == target: return [i+1, j+1]
            else: j -= 1