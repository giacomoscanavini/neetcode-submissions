class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Complexity Time: O(n) to traverse the string
        # Complexity Memory: O(n) to create the substring
        set_c = set()
        l_max = 0
        l = 0
        
        for j in range(len(s)):
            while s[j] in set_c:
                set_c.remove(s[l])
                l += 1
            set_c.add(s[j])
            l_max = max(l_max, j - l + 1)

        return l_max
        

        