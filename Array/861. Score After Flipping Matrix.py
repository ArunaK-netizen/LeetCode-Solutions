class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        for i in range(len(grid)):
            if (grid[i][0] == 0):
                for j in range(len(grid[i])):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
        cols = []
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cols.append(col)

        for i in range(len(cols)):
            if (cols[i].count(0) > cols[i].count(1)):
                for j in range(len(cols[i])):
                    if (cols[i][j] == 0):
                        cols[i][j] = 1
                    else:
                        cols[i][j] = 0
        rows = []
        for i in range(len(cols[0])):
            row = []
            for j in range(len(cols)):
                row.append(cols[j][i])
            rows.append(row)
        value = 0
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                value += rows[i][j] * (2 ** (len(rows[i]) - j - 1))
        return value


