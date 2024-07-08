class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer0 = []
        for i in range(len(nums1)):
            if (nums1[i] not in answer0 and nums1[i] not in nums2):
                answer0.append(nums1[i])

        answer1 = []
        for i in range(len(nums2)):
            if (nums2[i] not in answer1 and nums2[i] not in nums1):
                answer1.append(nums2[i])

        return [answer0, answer1]
