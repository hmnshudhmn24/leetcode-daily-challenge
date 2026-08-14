class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans, left = 0, 0
        counts = {}
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            while counts[s[right]] > 2:
                counts[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
