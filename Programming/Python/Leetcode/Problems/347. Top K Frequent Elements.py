"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
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
