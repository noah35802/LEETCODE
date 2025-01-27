class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        for char in range(26):
            c = chr(char + ord('a'))
            left = s.find(c)
            right = s.rfind(c)
            
            if left == -1: continue

            if right - left - 1 != distance[char]:
                return False
        
        return True
