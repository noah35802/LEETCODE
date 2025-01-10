class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        
        result = []
        n = len(nums)
        temp = n // 3
        
        i = 0
        while i < n:
            num = nums[i]
            count = 1
            while i + 1 < n and nums[i + 1] == num:
                i += 1
                count += 1
            if count > temp:
                result.append(num)
            i += 1
        
        return result
