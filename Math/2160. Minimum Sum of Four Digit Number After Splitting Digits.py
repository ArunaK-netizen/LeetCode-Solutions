class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        temp = num
        while(temp != 0):
            digits.append(temp % 10)
            temp = temp // 10
        digits = sorted(digits)
        return digits[0] * 10 + digits[-1] + digits[1]*10 + digits[-2]
