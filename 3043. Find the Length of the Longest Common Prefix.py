class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefixes = set()
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10
                
        ans = 0
        for num in arr2:
            while num > 0 and num not in prefixes:
                num //= 10
            if num > 0:
                ans = max(ans, len(str(num)))
                
        return ans
