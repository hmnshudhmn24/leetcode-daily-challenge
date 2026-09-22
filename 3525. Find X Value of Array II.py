from typing import List

class Node:
    def __init__(self, k: int):
        self.remain = [0] * k
        self.prod = 1

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)
        
    def merge(self, left: Node, right: Node) -> Node:
        node = Node(self.k)
        node.prod = (left.prod * right.prod) % self.k
        
        for i in range(self.k):
            node.remain[i] = left.remain[i]
            
        for i in range(self.k):
            idx = (i * left.prod) % self.k
            node.remain[idx] += right.remain[i]
            
        return node
        
    def build(self, nums: List[int], cur: int, left: int, right: int):
        if left == right:
            self.tree[cur].remain[nums[left]] = 1
            self.tree[cur].prod = nums[left]
            return
            
        mid = (left + right) // 2
        self.build(nums, 2 * cur + 1, left, mid)
        self.build(nums, 2 * cur + 2, mid + 1, right)
        self.tree[cur] = self.merge(self.tree[2 * cur + 1], self.tree[2 * cur + 2])
        
    def update(self, cur: int, lo: int, hi: int, i: int, val: int):
        if lo == hi:
            for j in range(self.k):
                self.tree[cur].remain[j] = 0
            self.tree[cur].remain[val] = 1
            self.tree[cur].prod = val
            return
            
        mid = (lo + hi) // 2
        if i <= mid:
            self.update(2 * cur + 1, lo, mid, i, val)
        else:
            self.update(2 * cur + 2, mid + 1, hi, i, val)
            
        self.tree[cur] = self.merge(self.tree[2 * cur + 1], self.tree[2 * cur + 2])
        
    def query(self, cur: int, lo: int, hi: int, i: int, j: int) -> Node:
        if i <= lo and hi <= j:
            return self.tree[cur]
        if j < lo or hi < i:
            return Node(self.k)
            
        mid = (lo + hi) // 2
        left_res = self.query(2 * cur + 1, lo, mid, i, j)
        right_res = self.query(2 * cur + 2, mid + 1, hi, i, j)
        return self.merge(left_res, right_res)

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] %= k
        for query in queries:
            query[1] %= k
            
        ans = []
        tree = SegmentTree(nums, k)
        
        for index, value, start, x in queries:
            tree.update(0, 0, n - 1, index, value)
            res = tree.query(0, 0, n - 1, start, n - 1)
            ans.append(res.remain[x])
            
        return ans
