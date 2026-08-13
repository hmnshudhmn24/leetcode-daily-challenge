from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree_size = 4 * n
        tree = [None] * tree_size

        def merge(L, R):
            if not L: return R
            if not R: return L
            mx = max(L[0], R[0])
            pre = L[1]
            suf = R[2]
            size = L[5] + R[5]
            if L[4] == R[3]:
                mx = max(mx, L[2] + R[1])
                if L[1] == L[5]: pre = L[5] + R[1]
                if R[2] == R[5]: suf = R[5] + L[2]
            return (mx, pre, suf, L[3], R[4], size)

        def build(node, start, end, chars):
            if start == end:
                tree[node] = (1, 1, 1, chars[start], chars[start], 1)
            else:
                mid = (start + end) // 2
                build(2*node, start, mid, chars)
                build(2*node+1, mid+1, end, chars)
                tree[node] = merge(tree[2*node], tree[2*node+1])

        def update(node, start, end, idx, char):
            if start == end:
                tree[node] = (1, 1, 1, char, char, 1)
            else:
                mid = (start + end) // 2
                if idx <= mid:
                    update(2*node, start, mid, idx, char)
                else:
                    update(2*node+1, mid+1, end, idx, char)
                tree[node] = merge(tree[2*node], tree[2*node+1])

        chars = list(s)
        build(1, 0, n-1, chars)

        res = []
        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n-1, idx, char)
            res.append(tree[1][0])
        return res
