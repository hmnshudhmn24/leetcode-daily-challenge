import collections
from typing import List

class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        # Prefix sum array (1-based for convenience)
        P = [0] * (n + 1)
        for i in range(n):
            P[i+1] = P[i] + nums[i]
        
        # dp[i] = max length ending at i
        dp = [0] * (n + 1)
        # last[i] = value of the last element ending at i
        last = [0] * (n + 1)
        
        # Deque stores indices. We maintain that (P[idx] + last[idx]) is increasing.
        dq = collections.deque([0])
        
        for i in range(1, n + 1):
            # Find best j
            while len(dq) > 1 and P[dq[1]] + last[dq[1]] <= P[i]:
                dq.popleft()
            
            j = dq[0]
            
            dp[i] = dp[j] + 1
            last[i] = P[i] - P[j]
            
            current_val = P[i] + last[i]
            while dq and P[dq[-1]] + last[dq[-1]] >= current_val:
                dq.pop()
            
            dq.append(i)
            
        return dp[n]
