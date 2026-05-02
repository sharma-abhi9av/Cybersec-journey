class Solution:
    def pivotInteger(self, n: int) -> int:
        number_list = list(range(1, n+1))
        for i in range(len(number_list)):
            if sum(number_list[:i+1])== sum(number_list[i:]):
                return number_list[i]
        return(-1)
