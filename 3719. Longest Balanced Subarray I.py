from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        
        # Iterate over every possible starting position
        for i in range(n):
            seen = set()
            even_cnt = 0
            odd_cnt = 0
            
            # Extend the subarray to the right
            for j in range(i, n):
                curr = nums[j]
                
                # Only process if the number is new to this subarray (distinct)
                if curr not in seen:
                    seen.add(curr)
                    if curr % 2 == 0:
                        even_cnt += 1
                    else:
                        odd_cnt += 1
                
                # Check if balanced
                if even_cnt == odd_cnt:
                    max_len = max(max_len, j - i + 1)
                    
        return max_len
