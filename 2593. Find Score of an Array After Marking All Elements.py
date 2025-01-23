class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        look=[0]*(len(nums)+1)
        ans=0
        for a,i in sorted([a,i] for i,a in enumerate(nums)):
            if look[i]:
                continue

            ans+=a
            look[i]=look[i-1]=look[i+1]=1

        return ans       
        
