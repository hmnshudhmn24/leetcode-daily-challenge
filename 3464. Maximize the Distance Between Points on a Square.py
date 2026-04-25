class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        def map_1d(x: int, y: int) -> int:
            if y == 0:
                return x
            if x == side:
                return side + y
            if y == side:
                return 3 * side - x
            return 4 * side - y

        P = sorted([map_1d(x, y) for x, y in points])
        n = len(P)
        A = P + [p + 4 * side for p in P]

        K_jumps = k - 1
        log_k = K_jumps.bit_length()

        low = 1
        high = (4 * side) // k
        ans = 0

        while low <= high:
            d = (low + high) // 2

            nxt = [0] * (2 * n + 1)
            j = 0
            for i in range(2 * n):
                while j < 2 * n and A[j] - A[i] < d:
                    j += 1
                nxt[i] = j
            nxt[2 * n] = 2 * n

            up = [nxt]
            for _ in range(1, log_k):
                prev = up[-1]
                up.append([prev[prev[idx]] for idx in range(2 * n + 1)])

            possible = False
            for i in range(n):
                curr = i
                for step in range(log_k):
                    if (K_jumps >> step) & 1:
                        curr = up[step][curr]

                if curr < 2 * n and A[curr] - A[i] <= 4 * side - d:
                    possible = True
                    break

            if possible:
                ans = d
                low = d + 1
            else:
                high = d - 1

        return ans
