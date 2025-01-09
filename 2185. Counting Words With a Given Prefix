class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        prefLen = len(pref)
        for word in words:
            if len(word) >= prefLen:
                if word[:prefLen] == pref:
                    count += 1
        return count
        
