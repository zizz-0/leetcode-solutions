from typing import List
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

"""
Runtime:
    15ms
    Beats 18.60%
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elems = {}
        ret = 0
        majority = 0
        for n in nums:
            elems[n] = 1 + elems.get(n, 0)
            if elems[n] > majority:
                ret = n
                majority = elems[n]
            
        return ret
        