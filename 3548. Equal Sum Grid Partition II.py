class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        total_sum = sum(map(sum, grid))

        def can_partition(g: list[list[int]]) -> bool:
            top_sum = 0
            seen = set()
            for i in range(len(g) - 1):
                top_sum += sum(g[i])
                bot_sum = total_sum - top_sum
                seen.update(g[i])
                diff = top_sum - bot_sum

                if diff == 0:
                    return True
                if diff in (g[0][0], g[0][-1], g[i][0], g[i][-1]):
                    return True
                if len(g[0]) > 1 and i > 0 and diff in seen:
                    return True

            return False

        def transposed(g: list[list[int]]) -> list[list[int]]:
            return [list(col) for col in zip(*g)]

        def reversed_grid(g: list[list[int]]) -> list[list[int]]:
            return g[::-1]

        return (can_partition(grid) or 
                can_partition(reversed_grid(grid)) or 
                can_partition(reversed_grid(transposed(grid))) or 
                can_partition(transposed(grid)))
