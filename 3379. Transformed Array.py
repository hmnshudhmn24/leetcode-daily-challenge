class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        
        for i in range(n):
            # Calculate the new index using modulo for circular wrapping.
            # Python's % operator handles negative numbers correctly.
            # e.g., if i=1, nums[i]=-2, n=4 -> (1 - 2) % 4 = -1 % 4 = 3
            target_index = (i + nums[i]) % n
            result.append(nums[target_index])
            
        return result
