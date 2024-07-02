class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWords = 0
        for i in sentences:
            if(len(i.split()) > maxWords):
                maxWords = len(i.split())
        return maxWords