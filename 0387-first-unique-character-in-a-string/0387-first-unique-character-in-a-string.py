class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = [i, 0]
            else:
                dic[s[i]][1] += 1
        for c in dic:
            if dic[c][1] == 0:
                return dic[c][0]
        return -1
            
            