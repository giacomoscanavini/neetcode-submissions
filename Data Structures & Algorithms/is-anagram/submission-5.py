class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time complexity: loop over elements O(n)
        # Space complexity: create hash map O(n)
        hash_s = {}
        for c in s: hash_s[c] = hash_s.get(c, 0) + 1
        for c in t: hash_s[c] = hash_s.get(c, 0) - 1
        
        for key in hash_s.keys():
            if hash_s[key] != 0: return False
        
        return True