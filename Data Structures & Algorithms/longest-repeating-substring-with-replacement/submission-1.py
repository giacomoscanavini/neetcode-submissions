class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Complexity Time: O(n) to traverse the array
        # Complexity Memory: O(n) to create the hash table
        hash_map = {}
        max_length = 0

        i = 0
        max_f = 0
        for j in range(len(s)):
            hash_map[s[j]] = hash_map.get(s[j], 0) + 1
            max_f = max(max_f, hash_map[s[j]])

            while (j - i + 1) - max_f > k:
                hash_map[s[i]] -= 1
                i += 1
            max_length = max(max_length, j - i + 1)
        return max_length
        