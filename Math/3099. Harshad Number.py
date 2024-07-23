class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sumDigits = 0
        temp = x
        while(temp!=0):
            sumDigits += temp % 10
            temp = temp // 10
        if(x % sumDigits == 0):
            return sumDigits
        return -1 