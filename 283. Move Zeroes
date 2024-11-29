class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        element = len(nums)
        j = 0
        for i in range(element):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j = j + 1
