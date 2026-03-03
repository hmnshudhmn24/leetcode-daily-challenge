class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = {}
        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            counts[digit_sum] = counts.get(digit_sum, 0) + 1
            
        max_size = max(counts.values())
        return sum(1 for v in counts.values() if v == max_size)
