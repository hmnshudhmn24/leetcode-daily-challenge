class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half = sorted(s[:n // 2])
        return "".join(half + ([s[n // 2]] if n % 2 else []) + half[::-1])
