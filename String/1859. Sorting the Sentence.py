class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        answer = sorted(s, key=lambda i: i[-1])
        final = []
        for i in answer:
            i = i[:-1]
            final.append(i)
        return " ".join(final)
