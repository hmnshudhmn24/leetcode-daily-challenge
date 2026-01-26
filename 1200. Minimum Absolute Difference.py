from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        arr.sort()

        min_diff = float('inf')
        result = []

        # Step 2: Single pass to find min_diff and collect pairs
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]

            if diff < min_diff:
                # Found a new minimum, reset the result list
                min_diff = diff
                result = [[arr[i], arr[i + 1]]]
            elif diff == min_diff:
                # Found another pair with the same minimum difference
                result.append([arr[i], arr[i + 1]])

        return result
