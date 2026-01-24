class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Step 1: Sort the array
        nums.sort()
        
        max_sum = 0
        n = len(nums)
        
        # Step 2: Pair smallest with largest
        for i in range(n // 2):
            current_sum = nums[i] + nums[n - 1 - i]
            max_sum = max(max_sum, current_sum)
            
        return max_sum
