class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)  # FIX: used len(nums) instead of nums.len()
        k_index = nums.index(k)
        
        # Map to store frequencies of balances on the left side
        # key: balance, value: count
        # Initialize with {0: 1} to represent the subarray containing only k itself
        left_counts = {0: 1}
        
        balance = 0
        # Scan Left from k-1 to 0
        for i in range(k_index - 1, -1, -1):
            if nums[i] < k:
                balance -= 1
            else:
                balance += 1
            left_counts[balance] = left_counts.get(balance, 0) + 1
            
        ans = 0
        balance = 0
        
        # Scan Right from k to n-1
        for i in range(k_index, n):
            if nums[i] < k:
                balance -= 1
            elif nums[i] > k:
                balance += 1
            
            # For odd length subarrays: left + right = 0  => left = -right
            ans += left_counts.get(-balance, 0)
            
            # For even length subarrays: left + right = 1  => left = 1 - right
            ans += left_counts.get(1 - balance, 0)
            
        return ans
