class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = ""
        ones = 0
        left = 0
        for right in range(len(s)):
            if s[right] == '1':
                ones += 1
            while ones == k:
                sub = s[left:right+1]
                if not res or len(sub) < len(res) or (len(sub) == len(res) and sub < res):
                    res = sub
                if s[left] == '1':
                    ones -= 1
                left += 1
        return res
