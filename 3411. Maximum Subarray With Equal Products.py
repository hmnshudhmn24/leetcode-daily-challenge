from math import gcd, lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        for i in range(n):
            curr_prod = 1
            curr_gcd = nums[i]
            curr_lcm = nums[i]
            for j in range(i, n):
                curr_prod *= nums[j]
                curr_gcd = gcd(curr_gcd, nums[j])
                curr_lcm = lcm(curr_lcm, nums[j])
                
                if curr_prod == curr_gcd * curr_lcm:
                    max_len = max(max_len, j - i + 1)
                elif curr_prod > curr_gcd * curr_lcm * 100:
                    break
        return max_len
