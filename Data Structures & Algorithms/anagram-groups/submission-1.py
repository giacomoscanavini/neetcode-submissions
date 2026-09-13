class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Complexity Time: O(n * c)
        # Complexity Memory: O(n) to create the dictionary
        dicts = {}

        for string in strs:
            key = [0] * 26
            for c in string:
                c_idx = ord(c) - ord('a')
                key[c_idx] += 1

            key = tuple(key)
            dicts[key] = dicts.get(key, [])
            dicts[key].append(string)


        return [value for key,value in dicts.items()]