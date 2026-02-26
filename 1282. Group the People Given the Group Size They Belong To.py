from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        res = []
        groups = defaultdict(list)
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                res.append(groups[size])
                groups[size] = []
        return res
