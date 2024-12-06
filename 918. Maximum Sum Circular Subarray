class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        maxSum, currentSum = nums[0], nums[0]
        for i in range(1, n):
            currentSum = max(nums[i], currentSum + nums[i])
            maxSum = max(maxSum, currentSum)
        
        minSum, currentSum = nums[0], nums[0]
        for i in range(1, n):
            currentSum = min(nums[i], currentSum + nums[i])
            minSum = min(minSum, currentSum)
        
        totalSum = sum(nums)
        if totalSum == minSum:  
            return maxSum
        return max(maxSum, totalSum - minSum)
        
