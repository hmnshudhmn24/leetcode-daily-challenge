import heapq

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        # Doubly Linked List simulation
        L = [-1] * n
        R = [-1] * n
        valid = [True] * n
        
        for i in range(n):
            L[i] = i - 1
            R[i] = i + 1 if i < n - 1 else -1
        
        bad_count = 0
        pq = []
        
        def is_inverted(i, j):
            if i == -1 or j == -1:
                return 0
            return 1 if nums[i] > nums[j] else 0
        
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                bad_count += 1
            heapq.heappush(pq, (nums[i] + nums[i + 1], i))
        
        if bad_count == 0:
            return 0
        
        ops = 0
        
        while bad_count > 0 and pq:
            curr_sum, i = heapq.heappop(pq)
            
            if not valid[i]:
                continue
            
            j = R[i]
            if j == -1:
                continue
            
            if nums[i] + nums[j] != curr_sum:
                continue
            
            p = L[i]
            nn = R[j]
            
            bad_count -= is_inverted(p, i)
            bad_count -= is_inverted(i, j)
            bad_count -= is_inverted(j, nn)
            
            nums[i] += nums[j]
            
            valid[j] = False
            R[i] = nn
            if nn != -1:
                L[nn] = i
            
            bad_count += is_inverted(p, i)
            bad_count += is_inverted(i, nn)
            
            if nn != -1:
                heapq.heappush(pq, (nums[i] + nums[nn], i))
            if p != -1:
                heapq.heappush(pq, (nums[p] + nums[i], p))
            
            ops += 1
        
        return ops
