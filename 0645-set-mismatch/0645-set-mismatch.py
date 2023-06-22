from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numbers = set([i+1 for i in range(len(nums))])
        count = Counter(nums)
        nums = set(nums)
        error = numbers - nums
        result = []
        for key, value in count.items():
            if value == 2:
                result.append(key)
                break
        result.append(list(error)[0])
        return result
                