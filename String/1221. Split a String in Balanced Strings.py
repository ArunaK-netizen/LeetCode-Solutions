class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        key = s[0]
        answer = 0
        i = 0
        while (i < len(s)):
            if (s[i] == key):
                count += 1
            else:
                count -= 1
            if (count == 0):
                answer += 1
            i += 1
        return answer
