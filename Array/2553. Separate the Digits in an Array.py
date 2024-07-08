class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            element = nums[i]
            digits = []
            while element != 0:
                digit = element % 10
                digits.append(digit)
                element = element // 10
            for i in digits[::-1]:
                answer.append(i)
        return answer
