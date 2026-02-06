from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n  # Track number of connected components

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by size
            if self.size[rootX] < self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
            self.count -= 1  # Decrement component count
            return True
        return False

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # Edge Case 1: Single element is always valid
        if n == 1:
            return True
            
        # Edge Case 2: If 1 exists in a multi-element array, it can never connect
        if 1 in nums:
            return False
        
        # Sort and remove duplicates
        nums = sorted(list(set(nums)))
        n = len(nums)
        
        if n == 1:
            return True
        
        # Initialize DSU
        dsu = UnionFind(n)
        
        # Map each prime to the first index containing it
        prime_to_index = {}
        
        for i, num in enumerate(nums):
            temp = num
            d = 2
            while d * d <= temp:
                if temp % d == 0:
                    if d in prime_to_index:
                        dsu.union(i, prime_to_index[d])
                    else:
                        prime_to_index[d] = i
                    
                    while temp % d == 0:
                        temp //= d
                d += 1
            
            if temp > 1:
                if temp in prime_to_index:
                    dsu.union(i, prime_to_index[temp])
                else:
                    prime_to_index[temp] = i
        
        return dsu.count == 1
