class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time complexity: 
        # Space complexity: 
        output = {}

        for string in strs:
            key = [0] * 26
            for c in string:
                idx = 'abcdefghijklmnopqrstuvwxyz'.index(c)
                key[idx] += 1
            key = tuple(key)
            if not output.get(key, 0):
                output[key] = [string]
            else:
                output[key].append(string)

        final_list = []
        for key in output.keys():
            final_list.append(output[key])
        return final_list