class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = []
        for i in range(len(names)):
            pairs.append([heights[i], names[i]])

        pairs = sorted(pairs, key=lambda pair: pair[0], reverse=True)
        answer = []
        for i in pairs:
            answer.append(i[1])
        return answer
