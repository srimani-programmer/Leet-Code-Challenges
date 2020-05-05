class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(0, len(s)):
            if(s.count(s[i]) == 1):
                return i
        return -1
        
s = input()
s1 = Solution()
print(s1.firstUniqChar(s))