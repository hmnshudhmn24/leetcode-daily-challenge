class Solution:
    def countTime(self, time: str) -> int:
        ans = 0
        for h in range(24):
            for m in range(60):
                s = f"{h:02d}:{m:02d}"
                if all(time[i] == '?' or time[i] == s[i] for i in range(5)):
                    ans += 1
        return ans
