class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        while count < k:
            max_index = 0
            for i in range(1, len(gifts)):
                if gifts[i] > gifts[max_index]:
                    max_index = i
            max_gift = gifts[max_index]
            new_gift = int(max_gift ** 0.5)
            gifts[max_index] = new_gift
            count += 1
        total_gifts = sum(gifts)
        return total_gifts
