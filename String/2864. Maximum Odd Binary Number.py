class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        countDict = Counter(s)
        answer = ['0'] * len(s)

        answer[-1] = '1'
        countDict['1'] -= 1

        for i in range(countDict['1']):
            answer[i] = '1'

        return "".join(answer)
