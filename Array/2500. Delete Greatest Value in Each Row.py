class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        answer = 0
        n = len(grid[0])
        for i in range(n):
            delElements = []
            for j in grid:
                delElements.append(max(j))
                j.pop(j.index(max(j)))
            answer += max(delElements)
        return answer