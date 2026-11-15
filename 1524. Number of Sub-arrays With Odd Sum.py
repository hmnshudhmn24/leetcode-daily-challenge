class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd, even, ans, curr = 0, 1, 0, 0
        for x in arr:
            curr += x
            if curr % 2:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        return ans % (10**9 + 7)
