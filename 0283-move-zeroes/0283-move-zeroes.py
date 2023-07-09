from collections import deque
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = nums.count(0)
        for _ in range(zero):
            nums.remove(0)
        nums.extend([0]*zero)
            
            