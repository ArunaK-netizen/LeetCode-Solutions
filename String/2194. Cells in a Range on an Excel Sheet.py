class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        endRows = int(s[-1])
        endCols = ord(s[-2])
        startCols = ord(s[0])
        firstChr = ord(s[0])
        answer = []
        startRows = int(s[1])
        for i in range(startCols, endCols + 1):
            for j in range(startRows, endRows + 1):
                answer.append(chr(i) + f'{j}')
        return answer
