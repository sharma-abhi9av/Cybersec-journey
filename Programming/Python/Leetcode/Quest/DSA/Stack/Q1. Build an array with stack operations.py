class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_set = set(target)
        record = []
        for number in range(1,max(target)+1):
            record.append("Push")
            if number not in target_set:      
                record.append("Pop")
        return record
