class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        
        result = 0
        if len(x) < len(y):
            x = (len(y)-len(x))*'0' + x
        elif len(x) > len(y):
            y = (len(x)-len(y))*'0' + y
        
        for i in range(len(x)):
            if x[i] != y[i]:
                result += 1
                
        return result
        