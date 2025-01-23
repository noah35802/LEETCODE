class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        for num in nums:
            if nums.count(num)==1:
                sum+=num
        return sum
