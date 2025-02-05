class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        swap_index = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if len(swap_index) == 2:
            i, j = swap_index
            return s1[i] == s2[j] and s1[j] == s2[i]
        return False
