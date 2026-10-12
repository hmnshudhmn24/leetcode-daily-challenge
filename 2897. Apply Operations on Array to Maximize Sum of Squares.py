from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 32
        
        for x in nums:
            for i in range(32):
                if (x >> i) & 1:
                    bit_counts[i] += 1
                    
        ans = 0
        for _ in range(k):
            num = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    num |= (1 << i)
                    bit_counts[i] -= 1
            ans = (ans + num * num) % MOD
            
        return ans
