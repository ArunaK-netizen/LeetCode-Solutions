class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for i in range(len(groupSizes)):
            groups[groupSizes[i]] = []

        for i in range(len(groupSizes)):
            groups[groupSizes[i]].append(i)
        print(groups)
        res = []
        for i in groups:
            for j in range(len(groups[i]) // i):
                res.append((groups[i])[i * j:i + i * j])

        return res
