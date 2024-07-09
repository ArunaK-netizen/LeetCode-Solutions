class Solution:
    def maxDepth(self, s: str) -> int:
        answer = 0
        count = 0
        for i in range(len(s)):
            if (s[i] == "("):
                count += 1
            elif (s[i] == ")"):
                count -= 1
            if (count > answer):
                answer = count
        return answer
