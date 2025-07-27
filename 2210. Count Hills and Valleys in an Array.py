class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        filtered = [nums[0]]
        for num in nums[1:]:
            if num != filtered[-1]:
                filtered.append(num)
        
        count = 0
        for i in range(1, len(filtered) - 1):
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                count += 1
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                count += 1
        
        return count
