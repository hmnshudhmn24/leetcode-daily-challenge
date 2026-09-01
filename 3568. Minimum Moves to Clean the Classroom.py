from collections import deque

class Solution:
    def minMoves(self, classroom: list[list[str]], energy: int) -> int:
        R, C = len(classroom), len(classroom[0])
        litter_pos = {}
        litter_idx = 0
        start_r = start_c = 0

        for r in range(R):
            for c in range(C):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_pos[(r, c)] = litter_idx
                    litter_idx += 1

        if litter_idx == 0:
            return 0

        target = (1 << litter_idx) - 1
        best_e = [[[-1] * (1 << litter_idx) for _ in range(C)] for _ in range(R)]

        q = deque([(start_r, start_c, energy, 0, 0)])
        best_e[start_r][start_c][0] = energy

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c, e, mask, dist = q.popleft()

            if e == 0:
                continue

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and classroom[nr][nc] != 'X':
                    nmask = mask
                    if (nr, nc) in litter_pos:
                        nmask |= (1 << litter_pos[(nr, nc)])

                    if nmask == target:
                        return dist + 1

                    ne = energy if classroom[nr][nc] == 'R' else e - 1

                    if ne >= 0 and ne > best_e[nr][nc][nmask]:
                        best_e[nr][nc][nmask] = ne
                        q.append((nr, nc, ne, nmask, dist + 1))

        return -1
