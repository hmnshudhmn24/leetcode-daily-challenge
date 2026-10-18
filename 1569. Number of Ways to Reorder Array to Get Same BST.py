from typing import List
import math


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def solve(arr):
            if len(arr) < 3:
                return 1

            root = arr[0]
            left_nodes = [x for x in arr if x < root]
            right_nodes = [x for x in arr if x > root]

            left_ways = solve(left_nodes)
            right_ways = solve(right_nodes)

            combinations = math.comb(
                len(left_nodes) + len(right_nodes),
                len(left_nodes)
            )

            return (left_ways * right_ways * combinations) % MOD

        return (solve(nums) - 1) % MOD
