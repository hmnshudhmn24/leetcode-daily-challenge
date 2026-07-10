from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        p = sorted(range(n), key=lambda i: nums[i])

        fa = [[0] * 17 for _ in range(n)]

        j = 0
        for i in range(n):
            while nums[p[i]] - nums[p[j]] > maxDiff:
                j += 1
            fa[i][0] = j
            for k in range(1, 17):
                fa[i][k] = fa[fa[i][k - 1]][k - 1]

        mp = [0] * n
        for i in range(n):
            mp[p[i]] = i

        ans = []
        for u, v in queries:
            a = mp[u]
            b = mp[v]

            if a < b:
                a, b = b, a

            s = 0
            for i in range(16, -1, -1):
                if fa[a][i] > b:
                    a = fa[a][i]
                    s |= (1 << i)

            if fa[a][0] > b:
                ans.append(-1)
            elif a != b:
                ans.append(s + 1)
            else:
                ans.append(0)

        return ans
