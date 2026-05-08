"""
Given two strings s and t, return true if t is an of s, and false otherwise.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        return Counter(t) == Counter(s)  
