class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0

            total = total + n
            max_sum = max(max_sum, total)
        
        return max_sum
        
