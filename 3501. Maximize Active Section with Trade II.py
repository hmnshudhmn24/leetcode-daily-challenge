import bisect

class SparseTable:
    def __init__(self, nums: list[int]):
        self.n = len(nums)
        if self.n == 0:
            return
        self.k = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(self.k)]
        for j in range(self.n):
            self.st[0][j] = nums[j]
        for i in range(1, self.k):
            for j in range(self.n - (1 << i) + 1):
                self.st[i][j] = max(self.st[i - 1][j], self.st[i - 1][j + (1 << (i - 1))])

    def query(self, l: int, r: int) -> int:
        if l > r or self.n == 0:
            return 0
        i = (r - l + 1).bit_length() - 1
        return max(self.st[i][l], self.st[i][r - (1 << i) + 1])

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        ones = s.count('1')
        n = len(s)
        G = []
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                G.append((start, i - 1))
            else:
                i += 1
        if not G:
            return [ones] * len(queries)
        ends = [g[1] for g in G]
        starts = [g[0] for g in G]
        adj_sums = []
        for j in range(len(G)-1):
            l1 = G[j][1] - G[j][0] + 1
            l2 = G[j+1][1] - G[j+1][0] + 1
            adj_sums.append(l1 + l2)
        st = SparseTable(adj_sums)
        def get_len(idx,l,r):
            return max(0, min(r,G[idx][1]) - max(l,G[idx][0]) + 1)
        ans=[]
        for l,r in queries:
            gs=bisect.bisect_left(ends,l)
            ge=bisect.bisect_right(starts,r)-1
            if gs>=ge:
                ans.append(ones)
            else:
                gain=max(get_len(gs,l,r)+get_len(gs+1,l,r), get_len(ge-1,l,r)+get_len(ge,l,r))
                ql=gs+1
                qr=ge-2
                if ql<=qr:
                    gain=max(gain, st.query(ql,qr))
                ans.append(ones+gain)
        return ans
