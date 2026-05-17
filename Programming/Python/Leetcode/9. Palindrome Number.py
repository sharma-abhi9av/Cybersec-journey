"""
Given an integer x, return true if x is a Palindrome, and false otherwise.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        mystr = f"{x}"
        return mystr == mystr[::-1]               
