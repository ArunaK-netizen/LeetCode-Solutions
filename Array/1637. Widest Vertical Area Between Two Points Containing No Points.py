class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda points: points[0])
        maxWidth = 0
        for i in range(len(points) - 1):
            if (points[i + 1][0] - points[i][0] > maxWidth):
                maxWidth = points[i + 1][0] - points[i][0]
        return maxWidth
