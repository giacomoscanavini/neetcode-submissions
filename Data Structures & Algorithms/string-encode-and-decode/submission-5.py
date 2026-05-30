class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        else:
            s = ''
            sizes = []
            for string in strs:
                sizes.append(str(len(string)))
            s = ','.join(sizes) + '¥' + ''.join(strs)
            return s

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: return []
        else:
            sizes, s = s.split('¥')
            sizes = sizes.split(',')
            sizes = [int(x) for x in sizes]

            strs = []
            for size in sizes:
                strs.append(s[:size])
                s = s[size:]

            return strs
