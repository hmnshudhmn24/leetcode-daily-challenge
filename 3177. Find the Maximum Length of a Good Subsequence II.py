from collections import defaultdict

class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        # dp[j][x] stores the max length of a sequence ending with 'x' with at most 'j' differences
        dp = [defaultdict(int) for _ in range(k + 1)]
        
        # max_len[j] stores the max length of any sequence with at most 'j' differences
        max_len = [0] * (k + 1)
        
        for num in nums:
            # Iterate backwards so we use the previous state's max_len 
            # without accidentally counting the current number twice
            for j in range(k, -1, -1):
                # Option 1: Append to a subsequence already ending in `num` (0 new differences)
                res = dp[j][num] + 1
                
                # Option 2: Append to the longest subsequence ending in a different number (1 new difference)
                if j > 0:
                    res = max(res, max_len[j - 1] + 1)
                
                # Update DP and global max trackers
                dp[j][num] = max(dp[j][num], res)
                max_len[j] = max(max_len[j], res)
                
        return max_len[k]
