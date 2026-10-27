class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Time complexity: Sorting O(n logn) + loop over the position array O(n)
        # Space complexity: Creation of fixed amount of arrays and the stack O(n)
        sorted_lists = sorted(zip(position, speed), key= lambda x: x[0], reverse=True)
        position, speed = zip(*sorted_lists)

        stack = []
        for i in range(len(position)):
            currentTime = (target - position[i]) / speed[i]
            
            if i == 0: 
                stack.append(currentTime)
            elif stack[-1] < currentTime: 
                stack.append(currentTime)

        return len(stack)