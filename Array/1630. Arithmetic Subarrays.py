class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checkDifference(arr):
            arr = sorted(arr)
            diff = arr[1] - arr[0]
            for i in range(len(arr) - 1):
                if (arr[i + 1] - arr[i] != diff):
                    return False
            return True

        boolArr = []
        for i in range(len(l)):
            checkArr = nums[l[i]:r[i] + 1]
            if (checkDifference(checkArr)):
                boolArr.append(True)
            else:
                boolArr.append(False)
        return boolArr
