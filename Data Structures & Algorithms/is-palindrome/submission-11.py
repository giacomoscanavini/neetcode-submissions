class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time complexity: Loop over characters of the string O(n)
        # Space complexity: Create a fixed number of variables O(1)
        i = 0
        j = len(s) - 1
        while i < j: 
            if not s[i].isalnum(): 
                i += 1
                continue

            if not s[j].isalnum(): 
                j -= 1
                continue

            if s[i].lower() != s[j].lower(): return False
            else:
                i += 1
                j -= 1

        return True


        