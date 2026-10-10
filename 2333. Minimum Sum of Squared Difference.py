class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]

        if sum(diffs) <= k:
            return 0

        max_diff = max(diffs)
        counts = [0] * (max_diff + 1)

        for d in diffs:
            counts[d] += 1

        for i in range(max_diff, 0, -1):
            if counts[i] == 0:
                continue
            take = min(counts[i], k)
            counts[i] -= take
            counts[i - 1] += take
            k -= take
            if k == 0:
                break

        return sum(i * i * counts[i] for i in range(1, max_diff + 1))
