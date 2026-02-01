import math
from typing import List

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        # Calculate GCD of all numbers in numsDivide
        g = numsDivide[0]
        for x in numsDivide[1:]:
            g = math.gcd(g, x)
        
        # Sort nums to check smallest candidates first
        nums.sort()
        
        for i, num in enumerate(nums):
            # If we find a number that divides the GCD, we stop
            if g % num == 0:
                return i
            # Optimization: If num > g, it can never divide g
            if num > g:
                break
                
        return -1
