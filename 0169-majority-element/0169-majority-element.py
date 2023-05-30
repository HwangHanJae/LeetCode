
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for num in set(nums):
            if nums.count(num) >= count:
                count = nums.count(num)
                result = num
        return result            