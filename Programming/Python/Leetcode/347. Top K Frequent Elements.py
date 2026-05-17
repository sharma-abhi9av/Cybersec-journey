"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        hashmap={}
        for num in nums : 
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        #print(hashmap)
        sorted_hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        #print(sorted_hashmap)
        keys_list = list(sorted_hashmap.keys())
        for i in range(k):
            output.append(keys_list[i])
        return(output)
