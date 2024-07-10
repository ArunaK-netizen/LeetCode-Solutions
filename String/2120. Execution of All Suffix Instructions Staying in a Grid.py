class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:

        gridLen = n
        answer = []
        for i in range(len(s)):
            startRow = startPos[0]
            startCol = startPos[1]
            count = 0
            for j in range(i, len(s)):
                if (s[j] == 'R' and startCol + 1 <= gridLen - 1):
                    count += 1
                    startCol += 1

                elif (s[j] == "D" and startRow + 1 <= gridLen - 1):
                    count += 1
                    startRow += 1

                elif (s[j] == "U" and startRow - 1 >= 0):
                    count += 1
                    startRow -= 1

                elif (s[j] == 'L' and startCol and startCol - 1 >= 0):
                    count += 1
                    startCol -= 1

                else:
                    break
            answer.append(count)

        return answer


