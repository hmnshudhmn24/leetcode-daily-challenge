class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                temp = nums[:i] + nums[j+1:]
                if all(temp[k] < temp[k+1] for k in range(len(temp)-1)):
                    ans += 1
        return ans
