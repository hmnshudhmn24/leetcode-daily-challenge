class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        visited = set()

        def dfs(i):
            if i < 0 or i >= len(arr) or i in visited:
                return False
            if arr[i] == 0:
                return True

            visited.add(i)
            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)
