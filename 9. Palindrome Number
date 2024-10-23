class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_number = 0
        original = x
        
        while x > 0:
            reversed_number = reversed_number * 10 + x % 10
            x //= 10
        
        return original == reversed_number
