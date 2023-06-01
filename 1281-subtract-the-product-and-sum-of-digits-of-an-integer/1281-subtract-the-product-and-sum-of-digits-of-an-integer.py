class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_num = 1
        sum_num = 0
        for i in str(n):
            i = int(i)
            product_num *= i
            sum_num += i
        
        return product_num - sum_num