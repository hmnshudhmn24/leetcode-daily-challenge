class SegmentTree:
    def __init__(self, n):
        self.n = n
        # tree_min and tree_max allow us to check if 0 exists in a range
        self.tree_min = [0] * (4 * n)
        self.tree_max = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _push(self, node):
        if self.lazy[node] != 0:
            add_val = self.lazy[node]
            # Apply to left child
            self.lazy[2 * node] += add_val
            self.tree_min[2 * node] += add_val
            self.tree_max[2 * node] += add_val
            # Apply to right child
            self.lazy[2 * node + 1] += add_val
            self.tree_min[2 * node + 1] += add_val
            self.tree_max[2 * node + 1] += add_val
            # Reset current
            self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if l > end or r < start:
            return
        if l <= start and end <= r:
            self.tree_min[node] += val
            self.tree_max[node] += val
            self.lazy[node] += val
            return
        
        self._push(node)
        mid = (start + end) // 2
        self.update(2 * node, start, mid, l, r, val)
        self.update(2 * node + 1, mid + 1, end, l, r, val)
        
        self.tree_min[node] = min(self.tree_min[2 * node], self.tree_min[2 * node + 1])
        self.tree_max[node] = max(self.tree_max[2 * node], self.tree_max[2 * node + 1])

    def find_first_zero(self, node, start, end, limit_r):
        # Optimization: If 0 is not in the min/max range, skip
        if self.tree_min[node] > 0 or self.tree_max[node] < 0:
            return -1
        # If out of query range
        if start > limit_r:
            return -1
            
        if start == end:
            return start if self.tree_min[node] == 0 else -1
            
        self._push(node)
        mid = (start + end) // 2
        
        # Try to find in the left child first (to get the longest subarray)
        res = self.find_first_zero(2 * node, start, mid, limit_r)
        if res != -1:
            return res
            
        # If not found in left, try right
        return self.find_first_zero(2 * node + 1, mid + 1, end, limit_r)


class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        st = SegmentTree(n)
        last_pos = {}
        ans = 0
        
        for r, x in enumerate(nums):
            # Determine contribution: Even = +1, Odd = -1
            val = 1 if x % 2 == 0 else -1
            
            # Find previous occurrence
            prev = last_pos.get(x, -1)
            
            # Update range [prev + 1, r]
            st.update(1, 0, n - 1, prev + 1, r, val)
            
            # Update the last position map
            last_pos[x] = r
            
            # Find the smallest l <= r where balance is 0
            l = st.find_first_zero(1, 0, n - 1, r)
            
            if l != -1:
                ans = max(ans, r - l + 1)
                
        return ans
