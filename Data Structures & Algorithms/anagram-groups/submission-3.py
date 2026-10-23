class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time complexity: loop over the strings * loop over each string O(n * m)
        # Space complexity: hash map O(m)
        output = {}

        for string in strs:
            key = [0] * 26
            for c in string:
                idx = 'abcdefghijklmnopqrstuvwxyz'.index(c.lower())
                key[idx] += 1
            key = tuple(key)
            if not output.get(key, 0):
                output[key] = [string]
            else:
                output[key].append(string)

        return list(output.values())