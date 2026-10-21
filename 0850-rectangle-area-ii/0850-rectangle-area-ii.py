class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        MOD = 10**9 + 7

        xs = sorted({x for x1, y1, x2, y2 in rectangles for x in (x1, x2)})
        ys = sorted({y for x1, y1, x2, y2 in rectangles for y in (y1, y2)})

        x_idx = {x: i for i, x in enumerate(xs)}
        y_idx = {y: i for i, y in enumerate(ys)}

        # grid[i][j] is True if the cell [xs[i], xs[i+1]] x [ys[j], ys[j+1]] is covered
        grid = [[False] * len(ys) for _ in range(len(xs))]

        for x1, y1, x2, y2 in rectangles:
            for i in range(x_idx[x1], x_idx[x2]):
                for j in range(y_idx[y1], y_idx[y2]):
                    grid[i][j] = True

        area = 0
        for i in range(len(xs) - 1):
            for j in range(len(ys) - 1):
                if grid[i][j]:
                    area += (xs[i + 1] - xs[i]) * (ys[j + 1] - ys[j])

        return area % MOD