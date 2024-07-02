class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        totalTime = 0
        lastG = lastM = lastP = 0
        for i, g in enumerate(garbage):
            totalTime += len(g)
            if 'G' in g:
                lastG = i
            if 'M' in g:
                lastM = i
            if 'P' in g:
                lastP = i

        totalTravel = 0
        for i in range(1, len(travel) + 1):
            if i <= lastG:
                totalTravel += travel[i - 1]
            if i <= lastM:
                totalTravel += travel[i - 1]
            if i <= lastP:
                totalTravel += travel[i - 1]

        return totalTime + totalTravel


