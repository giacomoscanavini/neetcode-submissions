class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Complexity Time: O(n) to traverse s2
        # Complexity Memory: O(m) to create a hash table up to len(s1)
        if len(s1) > len(s2): return False

        hash_s1 = {}
        for i in range(len(s1)):
            hash_s1[s1[i]] = hash_s1.get(s1[i], 0) + 1

        hash_s2 = {}
        l = 0
        for r in range(len(s2)):
            hash_s2[s2[r]] = hash_s2.get(s2[r], 0) + 1

            if sum(hash_s2.values()) < len(s1):
                continue
            elif sum(hash_s2.values()) > len(s1):
                hash_s2[s2[l]] -= 1
                if hash_s2[s2[l]] == 0: 
                    hash_s2.pop(s2[l])

                l += 1
            
            if hash_s1 == hash_s2: return True

        return False

            
        