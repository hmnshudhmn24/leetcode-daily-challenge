from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(mid):
            count, i = 0, 0
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k

        low, high = min(nums), max(nums)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
