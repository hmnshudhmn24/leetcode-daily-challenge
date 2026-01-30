import sys

class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        n = len(source)
        if len(target) != n:
            return -1

        # 1. Identify all unique substrings and map them to integer IDs
        nodes = set(original) | set(changed)
        mapping = {s: i for i, s in enumerate(nodes)}
        count = len(mapping)

        # Initialize distance matrix with infinity
        inf = float('inf')
        dist = [[inf] * count for _ in range(count)]

        # Distance to self is 0
        for i in range(count):
            dist[i][i] = 0

        # 2. Populate initial costs from the input arrays
        for o, c, z in zip(original, changed, cost):
            u, v = mapping[o], mapping[c]
            dist[u][v] = min(dist[u][v], z)

        # 3. Floyd-Warshall to find all-pairs shortest paths
        # Complexity: O(V^3) where V is the number of unique substrings (max ~200)
        for k in range(count):
            for i in range(count):
                if dist[i][k] == inf: continue
                for j in range(count):
                    if dist[k][j] == inf: continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Optimize lookup: Store valid transformation lengths to reduce DP iterations
        # Only lengths that actually appear in 'original' are candidates for replacement
        possible_lengths = set(len(s) for s in original)

        # 4. Dynamic Programming
        # dp[i] = min cost to convert source[:i] to target[:i]
        dp = [inf] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            # Option 1: Characters match perfectly, carry forward previous cost
            if source[i-1] == target[i-1]:
                dp[i] = dp[i-1]

            # Option 2: Try converting a suffix ending at i
            for length in possible_lengths:
                if i >= length:
                    start_idx = i - length
                    sub_s = source[start_idx:i]
                    sub_t = target[start_idx:i]

                    # If both substrings are known in our graph nodes
                    if sub_s in mapping and sub_t in mapping:
                        u, v = mapping[sub_s], mapping[sub_t]
                        # If a path exists between them
                        if dist[u][v] != inf:
                            if dp[start_idx] != inf:
                                dp[i] = min(dp[i], dp[start_idx] + dist[u][v])

        return dp[n] if dp[n] != inf else -1
