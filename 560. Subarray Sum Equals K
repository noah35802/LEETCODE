class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        dic = {0:1}
        res = 0
        for index, i in enumerate(nums):
            total += i
            
            if total-k in dic:
                res += dic[total-k]
                
            if total not in dic:
                dic[total] = 1
            else:
                dic[total] += 1

        return res 
