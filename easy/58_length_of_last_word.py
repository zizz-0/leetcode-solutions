"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

"""
Runtime:
    0ms
    Beats 100%
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splits = [spl for spl in s.split(" ") if spl != '']
        x = len(splits)
        return len(splits[x -1])