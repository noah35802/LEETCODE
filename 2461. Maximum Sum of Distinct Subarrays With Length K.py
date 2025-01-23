class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = set()
        n = len(nums)
        sum_ = 0
        mx = 0
        j = 0

        for i in range(n):
            while nums[i] in s:
                sum_ -= nums[j]
                s.remove(nums[j])
                j += 1
            
            s.add(nums[i])
            sum_ += nums[i]

            if len(s) == k:
                mx = max(mx, sum_)
                sum_ -= nums[j]
                s.remove(nums[j])
                j += 1

        return mx
