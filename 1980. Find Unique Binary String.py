class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        res = []
        for i in range(len(nums)):
            res.append("1" if nums[i][i] == "0" else "0")
        return "".join(res)
