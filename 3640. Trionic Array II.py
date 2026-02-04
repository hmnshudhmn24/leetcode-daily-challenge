import math

class Solution:
    def maxSumTrionic(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0
        
        # 1. Precompute L[i]: Max sum of strictly increasing subarray ending at i
        L = [0] * n
        L[0] = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                L[i] = max(nums[i], nums[i] + L[i-1])
            else:
                L[i] = nums[i]
                
        # 2. Precompute R[i]: Max sum of strictly increasing subarray starting at i
        R = [0] * n
        R[n-1] = nums[n-1]
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                R[i] = max(nums[i], nums[i] + R[i+1])
            else:
                R[i] = nums[i]
        
        # 3. Prefix Sums for O(1) range sum calculation
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
            
        ans = -math.inf
        
        # 4. Iterate through maximal decreasing segments
        i = 0
        while i < n - 1:
            if nums[i] > nums[i+1]:
                # Found start of a decreasing segment
                start = i
                while i < n - 1 and nums[i] > nums[i+1]:
                    i += 1
                end = i
                
                # Segment is nums[start...end]
                max_left_term = -math.inf
                
                # Iterate k from start to end
                for k in range(start, end + 1):
                    # Check if k can be a valid p (peak)
                    if k > 0 and nums[k] > nums[k-1]:
                        # Left Term: L[p-1] - prefix[p-1]
                        current_p_val = L[k-1] - prefix[k-1]
                        if current_p_val > max_left_term:
                            max_left_term = current_p_val
                    
                    # Check if k can be a valid q (valley)
                    # k must be > start to ensure p < q exists
                    if k > start and k < n - 1 and nums[k] < nums[k+1]:
                        # If we have a valid p before this q
                        if max_left_term != -math.inf:
                            # Right Term: R[q+1] + prefix[q]
                            current_q_val = R[k+1] + prefix[k]
                            total = max_left_term + current_q_val
                            if total > ans:
                                ans = total
            else:
                i += 1
                
        return ans if ans != -math.inf else 0
