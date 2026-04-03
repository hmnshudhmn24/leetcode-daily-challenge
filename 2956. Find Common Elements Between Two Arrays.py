class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1, set2 = set(nums1), set(nums2)
        return [sum(1 for x in nums1 if x in set2), sum(1 for x in nums2 if x in set1)]
