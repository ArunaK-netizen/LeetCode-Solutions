class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagSum = 0

        for i in range(len(mat)):
            diagSum += mat[i][i]
            diagSum += mat[i][len(mat) - i - 1]

        if len(mat) % 2 != 0:
            return diagSum - mat[len(mat) // 2][len(mat) // 2]

        return diagSum
