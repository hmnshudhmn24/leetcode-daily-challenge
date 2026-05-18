from typing import List
from collections import defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)

        curr = [0]
        visited = {0}
        step = 0

        while curr:
            nex = []
            for node in curr:
                if node == n - 1:
                    return step

                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                graph[arr[node]].clear()

                for child in [node - 1, node + 1]:
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curr = nex
            step += 1

        return -1
