"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        output={}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in output:
                output[sorted_word]= []
            output[sorted_word].append(word)
        return list(output.values())
