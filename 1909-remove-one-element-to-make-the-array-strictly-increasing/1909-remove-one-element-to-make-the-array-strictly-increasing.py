class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            array = nums[:i] + nums[i+1:]
            for j in range(len(array)-1):
                if array[j] >= array[j+1]:
                    break
            else:
                return True
        return False
                
                