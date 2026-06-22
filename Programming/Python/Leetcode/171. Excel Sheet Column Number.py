"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:
```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
```

Example 1:
```
Input: columnTitle = "A"
Output: 1
```
Example 2:
```
Input: columnTitle = "AB"
Output: 28
```
"""
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for num in columnTitle:
           ans = (ans * 26) + (ord(num) - 64)
        return(ans)
