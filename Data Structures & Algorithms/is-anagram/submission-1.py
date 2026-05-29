class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            # Single Hash map
            char_map = {}
            for c in s: char_map[c] = char_map.get(c, 0) + 1
            for c in t: char_map[c] = char_map.get(c, 0) - 1

            return all(c == 0 for c in char_map.values())

        
            