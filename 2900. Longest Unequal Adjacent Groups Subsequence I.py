class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        prev_group = -1
        for i in range(len(words)):
            if groups[i] != prev_group:
                result.append(words[i])
                prev_group = groups[i]
        return result
