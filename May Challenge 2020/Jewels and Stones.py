class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        for i in J:
            if(i in S):
                result += S.count(i)
        
        return result
        