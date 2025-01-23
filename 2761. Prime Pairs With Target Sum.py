class Solution(object):
    def findPrimePairs(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i * i, n + 1, i):
                    prime[j] = False
        
        prime_pairs = []
        for x in range(2, n // 2 + 1):
            y = n - x
            if prime[x] and prime[y]:
                prime_pairs.append([x, y])
        
        return prime_pairs
