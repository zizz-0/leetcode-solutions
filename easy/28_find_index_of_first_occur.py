"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

"""
Runtime:
    0ms
    Beats 100%
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        ind = 0
        i = 0
        x = 0

        while i < len(haystack) and x < len(needle):
            if haystack[i] != needle[x]:
                i = i - x + 1
                x = 0
            else:
                if x == 0:
                    ind = i
                x += 1
                i += 1

        return ind