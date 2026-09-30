class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # if len(s) == len(t):
        #    return anagram
        andi = Counter(s)
        mandi = Counter(t)
        count = 0
        for ch in andi:
            count += max(andi[ch] - mandi[ch], 0)
        for ch in mandi:
            count += max(mandi[ch] - andi[ch], 0)
        return count // 2
