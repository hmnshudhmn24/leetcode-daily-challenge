class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = curr = ans = 0
        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1]:
                curr += 1
            else:
                ans += min(prev, curr)
                prev = curr
                curr = 1
        ans += min(prev, curr)
        return ans
