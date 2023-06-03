class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []
        result = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        for i in range(len(nums) // 2):
            result.append(evens[i])
            result.append(odds[i])
        return result