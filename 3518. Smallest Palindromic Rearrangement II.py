class Solution:
    MAX_K = 1_000_001

    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half = s[:n // 2]
        mid = s[n // 2] if n % 2 == 1 else ""

        cnt = [0] * 26
        for c in half:
            cnt[ord(c) - ord('a')] += 1

        if self.count_arrangements(cnt) < k:
            return ""

        half_len = len(half)
        ans = []

        for _ in range(half_len):
            for i in range(26):
                if cnt[i] == 0:
                    continue
                cnt[i] -= 1
                ways = self.count_arrangements(cnt)
                if k <= ways:
                    ans.append(chr(ord('a') + i))
                    break
                cnt[i] += 1
                k -= ways

        left = "".join(ans)
        return left + mid + left[::-1]

    def count_arrangements(self, cnt: list[int]) -> int:
        total = sum(cnt)
        res = 1
        for c in cnt:
            if c == 0:
                continue
            res *= self.comb(total, c)
            if res >= self.MAX_K:
                return self.MAX_K
            total -= c
        return res

    def comb(self, n: int, k: int) -> int:
        k = min(k, n - k)
        res = 1
        for i in range(1, k + 1):
            res = res * (n - i + 1) // i
            if res >= self.MAX_K:
                return self.MAX_K
        return res
