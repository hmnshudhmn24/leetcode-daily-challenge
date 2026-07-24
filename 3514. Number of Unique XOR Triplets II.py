class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        u = list(set(nums))
        s1 = {u[i] ^ u[j] for i in range(len(u)) for j in range(i, len(u))}
        return len({v ^ x for v in s1 for x in u})
