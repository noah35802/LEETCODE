class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        current = 1
        for num in arr:
            while current < num:
                k -= 1
                if k == 0:
                    return current
                current += 1
            current = num + 1
        
        while k > 0:
            k -= 1
            if k == 0:
                return current
            current += 1
