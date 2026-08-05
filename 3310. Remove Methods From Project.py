import collections

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        seen = {k}
        q = collections.deque([k])

        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append(neighbor)

        for u in range(n):
            if u not in seen:
                for v in graph[u]:
                    if v in seen:
                        return list(range(n))

        return [i for i in range(n) if i not in seen]
