class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # 1. Edge case: If k is 1, the difference is always 0
        if k == 1:
            return 0
            
        # 2. Sort the scores to group closest numbers together
        nums.sort()
        
        # 3. Initialize minimum difference to infinity
        min_diff = float('inf')
        
        # 4. Use a sliding window to check differences
        # We iterate from index 0 up to len(nums) - k
        for i in range(len(nums) - k + 1):
            # The window is from i to i + k - 1
            # In a sorted window:
            #   Max value is at nums[i + k - 1]
            #   Min value is at nums[i]
            current_diff = nums[i + k - 1] - nums[i]
            
            # Update the global minimum
            min_diff = min(min_diff, current_diff)
            
        return min_diff
