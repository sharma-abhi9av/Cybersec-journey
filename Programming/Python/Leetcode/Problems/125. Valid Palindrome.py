"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True 
        i = 0 
        j = len(s)-1
        while i < j:
            if not s[i].isalnum():
                i +=1
            elif not s[j].isalnum():
                j -=1 
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False 
        return True
