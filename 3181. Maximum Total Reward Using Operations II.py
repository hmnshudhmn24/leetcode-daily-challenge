class Solution:
    def maxTotalReward(self, rewardValues: list[int]) -> int:
        rewardValues = sorted(set(rewardValues))
        valid_sums = 1
        for v in rewardValues:
            mask = (1 << v) - 1
            valid_sums |= (valid_sums & mask) << v
        return valid_sums.bit_length() - 1
