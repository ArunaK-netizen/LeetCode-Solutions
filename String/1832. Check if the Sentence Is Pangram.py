class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        countDict = Counter(sentence)
        for i in range(0, 26):
            if (chr(97 + i) not in countDict):
                return False
        return True

