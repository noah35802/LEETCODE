class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for word in words:
            for w in words:
                if word != w and word in w:
                    result.append(word)
                    break

        return result
