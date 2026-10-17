class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def get_digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        arr = [(x, i) for i, x in enumerate(nums)]
        arr.sort(key=lambda item: (get_digit_sum(item[0]), item[0]))

        n = len(nums)
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arr[i][1] == i:
                continue

            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr[j][1]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps
