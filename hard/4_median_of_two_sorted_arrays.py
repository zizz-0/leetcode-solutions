from typing import List
"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

"""
Runtime:
    2ms
    Beats 57.67%
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()

        med = (len(nums3) - 1) // 2

        if len(nums3) % 2 == 0:
            return ((nums3[med] + nums3[med + 1]) / 2)
        else:
            return nums3[med]