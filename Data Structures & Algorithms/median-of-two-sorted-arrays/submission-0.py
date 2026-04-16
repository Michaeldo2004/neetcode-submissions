class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        p1 = p2 = m1 = m2 = 0

        for i in range(n//2 +1):
            m2 = m1
            if p1 >= len(nums1): 
                m1 = nums2[p2]
                p2 += 1
            elif p2 >= len(nums2):
                m1 = nums1[p1]
                p1 += 1
            elif nums1[p1] >= nums2[p2]:
                m1 = nums2[p2]
                p2 += 1
            else:
                m1 = nums1[p1]
                p1 += 1
        
        if n%2: return m1
        else: return (m1 + m2)/2