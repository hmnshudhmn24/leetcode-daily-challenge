class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # 1. Initialize distance matrix
        # 26x26 grid for lowercase English letters
        inf = float('inf')
        dist = [[inf] * 26 for _ in range(26)]
        
        # Distance to self is always 0
        for i in range(26):
            dist[i][i] = 0
            
        # 2. Populate initial graph weights
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            # Handle multiple edges: keep the minimum cost
            dist[u][v] = min(dist[u][v], w)
            
        # 3. Floyd-Warshall Algorithm (All-Pairs Shortest Path)
        # Iterate through every possible intermediate node 'k'
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    # If going through k is cheaper, update the path
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    
        # 4. Calculate total cost
        total_cost = 0
        for s_char, t_char in zip(source, target):
            u = ord(s_char) - ord('a')
            v = ord(t_char) - ord('a')
            
            if dist[u][v] == inf:
                return -1
            
            total_cost += dist[u][v]
            
        return total_cost
