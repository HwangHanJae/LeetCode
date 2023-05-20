class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        result = 0
        vowel = ['a', 'e', 'i', 'o', 'u']
        prefix_sum = [0]
        for i in range(len(s)):
            if s[i] in vowel:
                prefix_sum.append(prefix_sum[-1] + 1)
            else:
                prefix_sum.append(prefix_sum[-1])
        
        for i in range(k, len(s)+1):
            result = max(result, prefix_sum[i] - prefix_sum[i-k])
        
        
        return result
            