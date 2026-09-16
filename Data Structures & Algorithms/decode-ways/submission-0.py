class Solution:
    def numDecodings(self, s: str) -> int:
        # Complexity Time: O(n) to traverse the array
        # Complexity Memory: O(1) to create a fixed set of variables
        ways = ways2 = 0
        ways1 = 1
        for i in range(len(s) - 1, -1, -1): 
            if s[i] == '0': 
                ways = 0
            else:
                ways = ways1

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                ways += ways2
            
            ways, ways1, ways2 = 0, ways, ways1

        return ways1