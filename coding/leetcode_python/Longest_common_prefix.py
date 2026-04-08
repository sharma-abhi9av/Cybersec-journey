class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # let's take the first word as reference
        first_word = strs[0]
        # the input can be empty so,
        if not strs :
          return("")
        # now for the puzzle --> we have the first word, let's first dig into it.
        for i, letter in enumerate(first_word):
            print(letter)  # now we have output as "f, l, o, w, e, r"
            # Next step should be checking the the letter of other words match.
            for a, word in enumerate(strs):
                if  a == len(word) or word[i] != first_word[i]:
                    return(first_word[:i])
        return first_word 
