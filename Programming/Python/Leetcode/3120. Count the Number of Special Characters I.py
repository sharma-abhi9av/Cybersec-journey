"""
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
Return the number of special letters in word.

Example 1:
```
Input: word = "aaAbcBC"
Output: 3
Explanation:
The special characters in word are 'a', 'b', and 'c'.
```
"""
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_set = set(word)
        output = 0 
        for letter in char_set: 
            if letter.islower():
                if letter.upper() in char_set:
                    output += 1 
        return output
