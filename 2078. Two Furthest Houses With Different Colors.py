class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        i, j = 0, n - 1

        while colors[j] == colors[0]:
            j -= 1

        while colors[i] == colors[-1]:
            i += 1

        return max(j, n - 1 - i)
