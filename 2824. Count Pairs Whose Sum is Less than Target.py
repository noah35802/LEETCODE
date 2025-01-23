class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        l,h,ans=0,len(nums)-1,0
        while l<h:
            val=nums[l]+nums[h]
            if val<target:
                ans+=(h-l)
                l+=1
            else:
                h-=1
        return ans
