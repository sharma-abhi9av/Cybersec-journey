"""
Given a string s, find the length of the longest without duplicate characters.

Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
```
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashtable = {}
        max_len = 0 
        left = 0 
        right = 0 
        while right < len(s):
            char = s[right]
            if char in hashtable and hashtable[char] >= left:
                left = hashtable[char] +1 
            
            hashtable[char] = right 
            
            if (right - left + 1) > max_len:
                max_len = (right - left +1 )
            right +=1              
        return max_len
