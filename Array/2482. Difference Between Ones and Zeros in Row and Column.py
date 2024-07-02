class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])

        onesRow = [sum(row) for row in grid]
        zerosRow = [m - ones for ones in onesRow]
        onesCol = [sum(grid[i][j] for i in range(n)) for j in range(m)]
        zerosCol = [n - ones for ones in onesCol]
        answer = [[onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j] for j in range(m)] for i in range(n)]

        return answer
