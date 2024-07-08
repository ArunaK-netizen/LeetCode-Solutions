class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        for i in paths:
            cities.add(i[0])

        for i in paths:
            if (i[1] not in cities):
                return i[1]





