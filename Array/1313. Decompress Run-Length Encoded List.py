class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums) // 2):
            freq, val = nums[2 * i], nums[2 * i + 1]
            for j in range(freq):
                answer.append(val)
        return answer
