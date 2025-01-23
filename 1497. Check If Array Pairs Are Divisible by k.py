class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_count = [0] * k
        
        for num in arr:
            remainder = num % k
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1
        
        if remainder_count[0] % 2 != 0:
            return False
        
        for r in range(1, (k // 2) + 1):
            if remainder_count[r] != remainder_count[k - r]:
                return False
        
        return True

solution = Solution()
arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
k = 5
print(solution.canArrange(arr, k))
