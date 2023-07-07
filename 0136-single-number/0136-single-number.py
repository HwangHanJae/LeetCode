from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        single = counter.most_common()[-1]
        if single[1] == 1:
            return single[0]
        
        
        