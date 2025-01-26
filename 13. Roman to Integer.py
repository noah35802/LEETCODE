class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        n = len(s)
        
        i = 0
        while i < n:
            if i < n - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                ans += roman_values[s[i + 1]] - roman_values[s[i]]
                i += 2
            else:
                ans += roman_values[s[i]]
                i += 1
        
        return ans
        
