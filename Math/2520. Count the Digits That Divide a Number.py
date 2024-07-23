class Solution:
    def countDigits(self, num: int) -> int:
        visited = set()
        digitsDividing = 0
        temp = num
        s = str(num)
        while(temp != 0):
            digit = temp % 10
            if(num % digit == 0 and digit not in visited):
                digitsDividing += s.count(str(digit))
                visited.add(digit)
            temp = temp // 10
        return digitsDividing