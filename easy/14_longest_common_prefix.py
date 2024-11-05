from typing import List
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

"""
Runtime:
    0ms
    Beats 100%
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0] # placeholder
        for word in strs:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

        return prefix