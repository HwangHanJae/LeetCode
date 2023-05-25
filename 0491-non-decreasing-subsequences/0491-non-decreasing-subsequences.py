from itertools import combinations
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        all_nums = set()
        for i in range(2, len(nums)+1):
            for sub in combinations(nums, i):
                if sub == tuple(sorted(sub)):
                    all_nums.add(sub)
        result = list(map(list, all_nums))
        
        return result