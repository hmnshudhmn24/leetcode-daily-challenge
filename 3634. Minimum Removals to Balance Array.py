import bisect
from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array to ensure contiguous subarrays represent valid ranges
        nums.sort()
        
        n = len(nums)
        max_kept = 0
        
        # Step 2: Iterate through each element treating it as the 'minimum' of the group
        for i in range(n):
            min_val = nums[i]
            max_allowed = min_val * k
            
            # Step 3: Find the rightmost index where elements are <= max_allowed
            j = bisect.bisect_right(nums, max_allowed)
            
            # Calculate the size of this valid window
            current_kept = j - i
            
            if current_kept > max_kept:
                max_kept = current_kept
        
        # Step 4: The result is total elements minus the maximum we can keep
        return n - max_kept
