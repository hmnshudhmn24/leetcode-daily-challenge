import bisect
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = sorted((intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n))
        starts = [x[0] for x in arr]
        
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            nxt = bisect.bisect_right(starts, arr[i][1])
            for count in range(1, 5):
                skip_w, skip_idx = dp[i + 1][count]
                
                take_next_w, take_next_idx = dp[nxt][count - 1]
                take_w = arr[i][2] + take_next_w
                take_idx = tuple(sorted((arr[i][3],) + take_next_idx))
                
                if take_w > skip_w:
                    dp[i][count] = (take_w, take_idx)
                elif take_w == skip_w:
                    dp[i][count] = (take_w, min(take_idx, skip_idx))
                else:
                    dp[i][count] = (skip_w, skip_idx)
                    
        return list(dp[0][4][1])
