class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for i in range(num1, num2 + 1):
            s = str(i)
            for j in range(1, len(s) - 1):
                if s[j - 1] < s[j] > s[j + 1] or s[j - 1] > s[j] < s[j + 1]:
                    ans += 1
        return ans
