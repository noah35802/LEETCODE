class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        unique_numbers = set()
        for i in range(len(digits)):
            if digits[i] == 0:
                continue
            for j in range(len(digits)):
                if i == j:
                    continue
                for k in range(len(digits)):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 == 0:
                        number = digits[i] * 100 + digits[j] * 10 + digits[k]
                        unique_numbers.add(number)
        return sorted(unique_numbers)
