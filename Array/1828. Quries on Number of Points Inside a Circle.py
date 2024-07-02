class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for j in queries:
            count = 0
            for i in points:
                eqVal = (i[0]-j[0])**2 + (i[1]-j[1]) ** 2
                if(eqVal <= j[2]**2):
                    count += 1
            answer.append(count)
        return answer