class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer1 = []
        answer2 = []
        for i in nums1:
            if(i in nums2):
                answer1.append(nums2.count(i))
                answer2.append(nums1.count(i))
        return [len(answer1), len(answer2)]