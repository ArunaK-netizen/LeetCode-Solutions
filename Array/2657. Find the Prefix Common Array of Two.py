class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        def countCommon(arr1, arr2):
            count = 0
            for i in range(len(arr1)):
                if (arr1[i] in arr2):
                    count += 1
            return count

        c = []
        for i in range(len(A)):
            numberCommon = countCommon(A[:i + 1], B[:i + 1])
            c.append(numberCommon)
        return c

