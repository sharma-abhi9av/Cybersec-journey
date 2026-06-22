"""
Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.
Answers within 10-5 of the actual value will be accepted as correct.

Example 1:
```
Input: hour = 12, minutes = 30
Output: 165
```
Example 2:
```
Input: hour = 3, minutes = 30
Output: 75
```
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float: 
        min = minutes * 6 
        if hour == 12:
            hour = 0
        hrs = ((hour*60) + minutes)  /2 
        ans = abs(min - hrs)
        if ans >180:
            return 360 - ans   
        return ans
