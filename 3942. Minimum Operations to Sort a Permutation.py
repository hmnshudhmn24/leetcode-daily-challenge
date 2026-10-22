from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = nums.index(0)

        asc = True
        for i in range(n):
            if nums[(zero + i) % n] != i:
                asc = False
                break

        desc = True
        for i in range(n):
            if nums[(zero - i) % n] != i:
                desc = False
                break

        ans = float('inf')

        if asc:
            ans = min(ans, zero, n - zero + 2)
        if desc:
            ans = min(ans, n - zero, zero + 2)

        return ans if ans != float('inf') else -1
