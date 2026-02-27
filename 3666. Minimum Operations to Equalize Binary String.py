import collections

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        start = s.count('0')
        if start == 0:
            return 0
            
        parent = list(range(n + 3))
        
        def find(i):
            root = i
            while parent[root] != root:
                root = parent[root]
            curr = i
            while curr != root:
                nxt = parent[curr]
                parent[curr] = root
                curr = nxt
            return root
            
        q = collections.deque([(start, 0)])
        parent[start] = find(start + 2)
        
        while q:
            u, steps = q.popleft()
            min_x = max(0, k - n + u)
            max_x = min(u, k)
            
            L = u + k - 2 * max_x
            R = u + k - 2 * min_x
            
            curr = find(L)
            while curr <= R:
                if curr == 0:
                    return steps + 1
                q.append((curr, steps + 1))
                parent[curr] = find(curr + 2)
                curr = find(curr)
                
        return -1
