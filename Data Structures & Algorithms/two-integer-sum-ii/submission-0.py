class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Complexity Time: 
        # Complexity Memory: 
        i, j = 0, len(numbers) - 1
        while i < j:
            sum_of_two = numbers[i] + numbers[j]
            if sum_of_two < target:
                i += 1
            elif sum_of_two > target:
                j -= 1
            else: 
                return [i+1, j+1]