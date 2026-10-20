class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True
            prev_max = float('-inf')

            for i in range(0, n, k):
                part = nums[i:i+k]

                chunk_min = min(part)
                if chunk_min < prev_max:
                    valid = False
                    break

                drops = 0
                for j in range(k - 1):
                    if part[j] > part[j+1]:
                        drops += 1
                        if drops > 1:
                            break

                if part[-1] > part[0]:
                    drops += 1

                if drops > 1:
                    valid = False
                    break

                prev_max = max(part)

            if valid:
                total += k

        return total
