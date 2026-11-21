import sys
sys.setrecursionlimit(200000)

class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
            
        ans = [0] * n
        d = {chr(i): [] for i in range(97, 123)}
        
        def dfs(i, fa):
            ans[i] = 1
            d[s[i]].append(i)
            
            for j in g[i]:
                dfs(j, i)
                
            k = fa
            if len(d[s[i]]) > 1:
                k = d[s[i]][-2]
                
            if k != -1:
                ans[k] += ans[i]
                
            d[s[i]].pop()
            
        dfs(0, -1)
        return ans
