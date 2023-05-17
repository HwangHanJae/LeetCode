class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        zero_index = []
        zero_count = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                zero_index.append(i+zero_count)
                zero_count += 1
        for i in zero_index:
            arr.insert(i, 0)
        
        for _ in range(len(arr) - n):
            arr.pop()
            
        
        
                
        