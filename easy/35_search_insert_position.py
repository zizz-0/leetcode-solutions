from typing import List

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

"""
Runtime:
    1ms
    Beats 5.89%
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ins = 0
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            if nums[i] < target:
                ins = i
                if i < len(nums) -1:
                    if i == 0 and nums[i + 1] > target:
                        return ins + 1
            if nums[i] > target:
                if i == 0:
                    return i
                return ins + 1
            i += 1
        return ins + 1