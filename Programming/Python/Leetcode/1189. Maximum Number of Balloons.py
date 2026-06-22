"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
```
Input: text = "nlaebolko"
Output: 1
```
Example 2:
```
Input: text = "loonbalxballpoon"
Output: 2
```
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashtable = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for letter in text :
            if letter in "balon":
                if letter in hashtable:
                    hashtable[letter] += 1 
                else : 
                    hashtable[letter] =1 
        hashtable["o"] //= 2
        hashtable["l"] //= 2
        return min(hashtable.values())
