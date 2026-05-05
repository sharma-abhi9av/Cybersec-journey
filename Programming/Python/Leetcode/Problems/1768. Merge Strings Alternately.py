"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length_of_word1, length_of_word2 = len(word1), len(word2)
        m,n = 0,0
        result= []
        while m <length_of_word1 or n <length_of_word2 :
            if m <length_of_word1:
                result += word1[m]
                m += 1
            if n <length_of_word2:
                result += word2[n]
                n += 1 
        return "".join(result)
  
