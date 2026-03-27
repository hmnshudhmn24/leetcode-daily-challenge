class Solution:
    def minimumRightShifts(self, nums: list[int]) -> int:
        dip_idx = -1
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                if dip_idx != -1:
                    return -1
                dip_idx = i
        if dip_idx == -1:
            return 0
        if nums[-1] > nums[0]:
            return -1
        return n - 1 - dip_idx
