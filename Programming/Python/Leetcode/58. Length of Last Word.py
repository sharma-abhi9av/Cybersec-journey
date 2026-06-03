"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal consisting of non-space characters only.
  
Example 1:
```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```
"""
# Version 1
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.strip()
        print(a)
        last = ""
        for word in a:
            if word in [" ","  ","   ","    ","     "]:
                last = ""
            elif word.isalpha():
                last +=word
        return len(last)


# Version 2 
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.strip()
        last = ""
        for word in a:
            if word ==" ":
                last = ""
            elif word.isalpha():
                last +=word
        return len(last)

# Final
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return(len(s.split()[-1]))
