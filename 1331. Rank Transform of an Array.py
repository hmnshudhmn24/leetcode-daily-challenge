class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        ranks = {val: i + 1 for i, val in enumerate(sorted(set(arr)))}
        return [ranks[x] for x in arr]
