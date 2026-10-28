class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time complexity: Loop over the string O(n)
        # Space complexity: Create hash map O(n)
        if len(s) == 0: return 0

        longest = 0
        sequence = {}
        l = 0
        for i,c in enumerate(s):
            if c in sequence:
                l = max(l, sequence[c] + 1)
            sequence[c] = i
            longest = max(longest, i - l + 1)
        return longest