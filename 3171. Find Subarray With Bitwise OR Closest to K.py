from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        prev = set()
        min_diff = float('inf')
        
        for num in nums:
            # Use the '|' operator to keep track of OR results
            prev = {num} | {num | p for p in prev}
            
            for val in prev:
                min_diff = min(min_diff, abs(val - k))
                
            # Early exit: we can't get a better difference than 0
            if min_diff == 0:
                return 0
                
        return min_diff
