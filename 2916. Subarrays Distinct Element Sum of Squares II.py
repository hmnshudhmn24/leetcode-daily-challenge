from typing import List

class SegmentTree:
    def __init__(self, n):
        self.sum_sq = [0] * (4 * n)
        self.sum_lin = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def push(self, node, l, r):
        if self.lazy[node] != 0:
            mid = (l + r) // 2
            lz = self.lazy[node]
            len_l = mid - l + 1
            self.sum_sq[2*node] = (self.sum_sq[2*node] + 2 * lz * self.sum_lin[2*node] + len_l * lz * lz) % self.MOD
            self.sum_lin[2*node] = (self.sum_lin[2*node] + len_l * lz) % self.MOD
            self.lazy[2*node] = (self.lazy[2*node] + lz) % self.MOD
            len_r = r - mid
            self.sum_sq[2*node+1] = (self.sum_sq[2*node+1] + 2 * lz * self.sum_lin[2*node+1] + len_r * lz * lz) % self.MOD
            self.sum_lin[2*node+1] = (self.sum_lin[2*node+1] + len_r * lz) % self.MOD
            self.lazy[2*node+1] = (self.lazy[2*node+1] + lz) % self.MOD
            self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if r < start or end < l:
            return
        if l <= start and end <= r:
            length = end - start + 1
            self.sum_sq[node] = (self.sum_sq[node] + 2 * val * self.sum_lin[node] + length * val * val) % self.MOD
            self.sum_lin[node] = (self.sum_lin[node] + length * val) % self.MOD
            self.lazy[node] = (self.lazy[node] + val) % self.MOD
            return
        self.push(node, start, end)
        mid = (start + end) // 2
        self.update(2*node, start, mid, l, r, val)
        self.update(2*node+1, mid+1, end, l, r, val)
        self.sum_sq[node] = (self.sum_sq[2*node] + self.sum_sq[2*node+1]) % self.MOD
        self.sum_lin[node] = (self.sum_lin[2*node] + self.sum_lin[2*node+1]) % self.MOD

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        st = SegmentTree(n)
        last_seen = {}
        total = 0
        for i, x in enumerate(nums):
            prev = last_seen.get(x, -1)
            st.update(1, 0, n - 1, prev + 1, i, 1)
            total = (total + st.sum_sq[1]) % MOD
            last_seen[x] = i
        return total
