class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        answer = []
        for i in l:
            answer.append(i[::-1])
        return " ".join(answer)
