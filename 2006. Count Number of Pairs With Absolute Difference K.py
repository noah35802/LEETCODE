class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
    	count = 0
    	for n in nums:
    	    freq[n]= freq.get(n, 0) + 1
    	    
        for n in nums:
            if n + k in freq:
                count += freq[n + k]
            if n - k in freq:
                count += freq[n -k]
            freq[n] -= 1
            
        return count
        
