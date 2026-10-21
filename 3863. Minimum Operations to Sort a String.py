class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if all(s[i] <= s[i+1] for i in range(n - 1)):
            return 0
        if n == 2:
            return -1

        min_c = max_c = 0
        for i in range(n):
            if s[i] < s[min_c]:
                min_c = i
            if s[i] >= s[max_c]:
                max_c = i

        if min_c == 0 or max_c == n - 1:
            return 1

        return 3 if min_c == n - 1 and max_c == 0 else 2
