class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        letterCount = dict(Counter(letters))
        print(letterCount)

        allWords = []
        scores = []
        for i in range(1 << len(words)):
            combination = []
            for j in range(len(words)):
                if i & (1 << j):
                    combination.append(words[j])
            allWords.append("".join(combination))

        for i in range(len(allWords)):
            curScore = 0
            for j in allWords[i]:
                if (j in letterCount and letterCount[j] > 0):
                    curScore += score[ord(j) - 97]
                    letterCount[j] -= 1
                else:
                    curScore = -1
                    break
            if (curScore != -1):
                scores.append(curScore)
            letterCount = dict(Counter(letters))

        if (len(scores)):
            return max(scores)
        return 0