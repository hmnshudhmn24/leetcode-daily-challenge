from typing import List
from sortedcontainers import SortedList


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # We need the smallest (k-1) elements in a sliding window of size (dist+1),
        # considering elements from nums[1:] onward.

        target_count = k - 1

        # L holds the smallest target_count elements
        # R holds the remaining elements in the window
        L = SortedList()
        R = SortedList()
        current_sum = 0

        def add(val: int):
            nonlocal current_sum
            if len(L) < target_count:
                L.add(val)
                current_sum += val
            elif val < L[-1]:
                largest = L.pop()
                current_sum -= largest
                R.add(largest)

                L.add(val)
                current_sum += val
            else:
                R.add(val)

        def remove(val: int):
            nonlocal current_sum
            if val in R:
                R.remove(val)
            else:
                L.remove(val)
                current_sum -= val
                if R:
                    smallest = R.pop(0)
                    L.add(smallest)
                    current_sum += smallest

        n = len(nums)
        window_len = dist + 1

        # Initialize first window
        for i in range(1, min(n, window_len + 1)):
            add(nums[i])

        ans = current_sum

        # Slide the window
        for i in range(window_len + 1, n):
            out_elem = nums[i - (dist + 1)]
            in_elem = nums[i]

            remove(out_elem)
            add(in_elem)

            ans = min(ans, current_sum)

        return ans + nums[0]
