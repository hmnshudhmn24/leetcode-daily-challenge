from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # The first element is always included
        cost = nums[0]
        
        # We need the two smallest elements from the rest of the array
        # Sort the slice nums[1:] and take the first two
        remaining = sorted(nums[1:])
        
        return cost + remaining[0] + remaining[1]
