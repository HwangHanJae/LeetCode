class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            num = str(num)
            for i in num:
                digit_sum += int(i)
        
        return abs(element_sum - digit_sum)