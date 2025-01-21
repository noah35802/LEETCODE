class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        left=moves.count('R')
        right=moves.count('L')
        space=moves.count('_')
        return abs(left-right)+space
