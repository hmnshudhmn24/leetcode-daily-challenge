from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        def check(length):
            M = (1 << 61) - 1
            B = 100003
            power = pow(B, length, M)
            curr = 0
            
            for i in range(length):
                curr = (curr * B + nums[i]) % M
                
            freq = {curr: 1}
            
            for i in range(length, n):
                curr = (curr * B + nums[i] - nums[i - length] * power) % M
                curr = (curr + M) % M
                freq[curr] = freq.get(curr, 0) + 1
                
            for count in freq.values():
                if count == 1:
                    return True
            return False

        left, right = 1, n
        ans = n
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans
