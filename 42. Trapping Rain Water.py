class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
            return 0
        
        trapped = 0
        
        i, j = 0, n - 1 # left and right

        left_max = height[i] #left to right pointer
        right_max = height[j] #right to left pointer
        trapped = 0

    

        while i < j:
            if left_max < right_max: #moving right
                i += 1
                left_max = max(left_max, height[i])
                trapped += left_max - height[i]

            else: #moving left
                right_max = max(right_max, height[j])
                trapped += right_max - height[j]
                j -= 1


        return trapped
