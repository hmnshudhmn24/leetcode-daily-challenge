class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        right_min = [0] * n
        right_min[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], nums[i])
            
        left_max = 0
        for i, val in enumerate(nums):
            left_max = max(left_max, val)
            if left_max - right_min[i] <= k:
                return i
                
        return -1
