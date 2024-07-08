class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [[0] * n for i in range(m)]
        for i in range(len(indices)):
            r = indices[i][0]
            c = indices[i][1]
            for j in range(n):
                mat[r][j] += 1

            for j in range(m):
                mat[j][c] += 1

        count = 0
        for i in mat:
            for j in i:
                if (j % 2 != 0):
                    count += 1
        return count

