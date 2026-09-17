class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        prefix_sums = {0: -1}
        curr_sum = 0
        min_len = [float('inf')] * len(arr)
        best = float('inf')
        ans = float('inf')
        
        for i, num in enumerate(arr):
            curr_sum += num
            if curr_sum - target in prefix_sums:
                start_idx = prefix_sums[curr_sum - target]
                length = i - start_idx
                if start_idx >= 0:
                    ans = min(ans, length + min_len[start_idx])
                best = min(best, length)
            min_len[i] = best
            prefix_sums[curr_sum] = i
            
        return ans if ans != float('inf') else -1
