class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        permutation = []
        for i in range(1, m + 1):
            permutation.append(i)

        answer = []
        for i in range(len(queries)):
            answer.append(permutation.index(queries[i]))
            t = permutation.pop(permutation.index(queries[i]))
            permutation.insert(0, t)

        return answer
