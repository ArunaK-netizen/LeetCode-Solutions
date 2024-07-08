class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        firstCounter = dict()
        secondCounter = dict()

        for i in range(len(s)):
            firstCounter[s[i]] = i
            secondCounter[t[i]] = i

        permDiff = 0
        for i in firstCounter:
            permDiff += abs(firstCounter[i] - secondCounter[i])
        return permDiff

