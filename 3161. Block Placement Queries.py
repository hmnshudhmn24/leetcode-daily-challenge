from sortedcontainers import SortedList

class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        ans = []
        limit = max(q[1] for q in queries) + 5
        bit = [0] * (limit + 1)

        def update(i: int, val: int):
            while i <= limit:
                bit[i] = max(bit[i], val)
                i += i & -i

        def query(i: int) -> int:
            res = 0
            while i > 0:
                res = max(res, bit[i])
                i -= i & -i
            return res

        sl = SortedList([0, limit])
        for q in queries:
            if q[0] == 1:
                sl.add(q[1])

        for i in range(1, len(sl)):
            update(sl[i], sl[i] - sl[i - 1])

        for q in reversed(queries):
            if q[0] == 1:
                idx = sl.index(q[1])
                nxt = sl[idx + 1]
                prv = sl[idx - 1]
                del sl[idx]
                update(nxt, nxt - prv)
            else:
                x, sz = q[1], q[2]
                idx = sl.bisect_right(x)
                prv = sl[idx - 1]
                ans.append(query(prv) >= sz or x - prv >= sz)

        return ans[::-1]
