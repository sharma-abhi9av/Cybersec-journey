"""
Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.
A substring is a contiguous sequence of characters within a string.

Example 1:
```
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
```
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.

Example 2:
```
Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
Output: 2
```
Explanation:
- "a" appears as a substring in "aaaaabbbbb".
- "b" appears as a substring in "aaaaabbbbb".
- "c" does not appear as a substring in "aaaaabbbbb".
2 of the strings in patterns appear as a substring in word.

"""

class TrieNode:
    def __init__(self):
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
            
    def is_there(self, pattern):
        curr = self.root        
        for letter in pattern:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return count
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        my_trie = Trie()
        for i in range(len(word)):
            my_trie.insert(word[i:])
        count = 0 
        for pattern in patterns:
            if my_trie.is_there(pattern):
                count +=1 
        return count
