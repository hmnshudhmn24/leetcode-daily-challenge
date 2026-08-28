from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        count = Counter(s)
        odds = [c for c, v in count.items() if v % 2 != 0]
        if len(odds) > 1:
            return ""

        mid = odds[0] if odds else ""
        avail = {c: v // 2 for c, v in count.items() if v // 2 > 0}
        n = len(s)
        half_len = n // 2
        res = []

        def dfs(i, is_greater):
            if i == half_len:
                left = "".join(res)
                pal = left + mid + left[::-1]
                return pal if pal > target else ""

            for c in sorted(avail.keys()):
                if avail[c] == 0:
                    continue
                if not is_greater and c < target[i]:
                    continue

                res.append(c)
                avail[c] -= 1

                ans = dfs(i + 1, is_greater or c > target[i])
                if ans:
                    return ans

                avail[c] += 1
                res.pop()

            return ""

        return dfs(0, False)
