class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff_needed = arr[1] - arr[0]
        for i in range(2,len(arr)):
            if (arr[i] - arr[i-1]) != diff_needed:
                return False
        return True
