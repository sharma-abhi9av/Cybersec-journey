"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```
Example 2:
```
Input: numRows = 1
Output: [[1]]
```
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        output = [[1]]
        
        for i in range(1, numRows):
            prev_row = output[-1]
            curr_row = [1]
            for j in range(1, i):
                curr_row.append(prev_row[j-1] + prev_row[j])
            curr_row.append(1)
            output.append(curr_row)
        return output

