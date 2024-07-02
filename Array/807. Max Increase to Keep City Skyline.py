class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = []
        colMax = []
        for i in range(len(grid)):
            rMax = 0
            cMax = 0
            for j in range(len(grid[i])):
                if (grid[i][j] > rMax):
                    rMax = grid[i][j]

                if (grid[j][i] > cMax):
                    cMax = grid[j][i]
            rowMax.append(rMax)
            colMax.append(cMax)
        maxInc = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] < rowMax[i] and grid[i][j] < colMax[j]):
                    maxInc += min(rowMax[i], colMax[j]) - grid[i][j]
        return maxInc

