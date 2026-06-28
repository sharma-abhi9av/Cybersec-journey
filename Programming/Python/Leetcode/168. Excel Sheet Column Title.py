"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:
```
Input: columnNumber = 1
Output: "A"
```
Example 2:
```
Input: columnNumber = 28
Output: "AB"
```
"""
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        
        while columnNumber > 0:
            columnNumber -= 1 
            remainder = columnNumber % 26
            char = chr(remainder + 65)
            result = char + result
            columnNumber //= 26        
        return result
