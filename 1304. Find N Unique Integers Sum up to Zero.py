class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        num, rem = n // 2, n % 2
        if rem != 0: ans = [0]
        else: ans = []
        for i in range(1,num+1):
            ans.append(-i)
            ans.append(i) 
        return ans
