class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        n = len(s)
        dp = [False] * n
        dp[0] = True
        available = 0

        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                available += 1
            if i > maxJump and dp[i - maxJump - 1]:
                available -= 1

            if available > 0 and s[i] == '0':
                dp[i] = True

        return dp[-1]
