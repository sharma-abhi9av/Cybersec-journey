"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # the input can be empty so,
        if not strs :
          return("")
        # let's take the first word as reference
        first_word = strs[0]
        # now for the puzzle --> we have the first word, let's first dig into it.
        for i, letter in enumerate(first_word):
            # print(letter) now we have output as "f, l, o, w, e, r"
            # Next step should be checking the the letter of other words match.
            for word in strs[1:]:
                if  i == len(word) or word[i] != letter:
                    return(first_word[:i])
        return first_word 
