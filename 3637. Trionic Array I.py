from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        # 1. Find first peak (p)
        i = 0
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
            
        # Check if we actually went up (p > 0) 
        # and didn't reach the end (must leave room for decrease and next increase)
        if i == 0 or i == n - 1:
            return False
        
        # 2. Find valley (q)
        while i < n - 1 and nums[i] > nums[i + 1]:
            i += 1
            
        # Check if we actually went down 
        # and didn't reach the end (must leave room for final increase)
        if nums[i - 1] <= nums[i] or i == n - 1:
            return False
            
        # 3. Check final ascent
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
            
        # If we reached the end, it's Trionic
        return i == n - 1
