class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        k = 0
        while True:		
            if k*word not in sequence:
                return k-1
            k = k + 1
