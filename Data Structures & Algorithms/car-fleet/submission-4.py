class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Time complexity: Sorting O(n logn) + multiple loops over the position array O(n)
        # Space complexity: Creation of fixed amount of arrays O(n)
        sorted_lists = sorted(zip(position, speed), key= lambda x: x[0], reverse=True)
        position, speed = zip(*sorted_lists)

        nFleets = 1
        previousTime = (target - position[0]) / speed[0]
        for i in range(1, len(position)):
            currentTime = (target - position[i]) / speed[i]
            if currentTime > previousTime:
                nFleets += 1
                previousTime = currentTime

        return nFleets