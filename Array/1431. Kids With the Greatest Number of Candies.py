class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = 0
        for i in candies:
            if (i > maxCandies):
                maxCandies = i
        res = []
        for i in candies:
            if (i + extraCandies >= maxCandies):
                res.append(True)
            else:
                res.append(False)
        return res
