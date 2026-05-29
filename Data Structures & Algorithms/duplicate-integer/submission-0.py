class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        content = {}
        for num in nums:
            content[num] = content.get(num, 0) + 1

            if content[num] > 1:
                return True
        return False
        