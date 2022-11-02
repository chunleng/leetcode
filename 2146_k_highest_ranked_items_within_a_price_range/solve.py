class Solution:
    def highestRankedKItems(self, grid: list[list[int]], pricing: list[int], start: list[int], k: int) -> list[list[int]]:
        seen = [[False for __ in range(len(grid[0]))] for _ in range(len(grid))]
        seen[start[0]][start[1]] = True
        q: list[tuple[int,int,int]] = [(0, start[0], start[1])]
        candidates = []

        X_LEN = len(grid)
        Y_LEN = len(grid[0])

        while q:
            current = q.pop(0)
            dist, x, y = current

            if pricing[0] <= grid[x][y] <= pricing[1]:
                candidates.append([dist, grid[x][y], x, y])

            dirs: list[tuple[int,int]] = [(-1,0), (1,0), (0,-1), (0,1)]
            if len(candidates) < k:
                # stop searching further if we have not found enough candidates
                for m,n in dirs:
                    x2 = x + m
                    y2 = y + n
                    if 0 <= x2 < X_LEN and 0 <= y2 < Y_LEN and grid[x2][y2] > 0 and not seen[x2][y2]:
                        q.append((dist+1, x2, y2))
                        seen[x2][y2] = True

        candidates.sort()
        return [c[2:] for c in candidates[:k]]
