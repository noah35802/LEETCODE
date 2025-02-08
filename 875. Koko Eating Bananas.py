class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def canFinish(speed):
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            return hours <= h
            
        left, right = 1, max(piles)
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            if canFinish(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return result
