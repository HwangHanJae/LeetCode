class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        while nums:
            num1 = nums.pop()
            num2 = nums.pop()
            if num1 != num2:
                return False
        return True
        