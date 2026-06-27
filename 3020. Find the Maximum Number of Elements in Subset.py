from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = cnt[1] - 1 if cnt[1] % 2 == 0 else cnt[1]
        ans = max(1, ans)

        seen = set()
        for x in cnt:
            if x == 1 or x in seen:
                continue

            curr_len = 0
            curr = x

            while cnt[curr] >= 2:
                seen.add(curr)
                curr_len += 2
                curr *= curr

            if cnt[curr] > 0:
                curr_len += 1
            else:
                curr_len -= 1

            ans = max(ans, curr_len)

        return ans
