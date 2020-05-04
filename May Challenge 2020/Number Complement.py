class Solution:
    def findComplement(self, num: int) -> int:
        binaryRepresentation = bin(num)
        binaryRepresentation = list(binaryRepresentation[2:])

        for i in range(0,len(binaryRepresentation)):
            if(binaryRepresentation[i] == '1'):
                binaryRepresentation[i] = '0'
            else:
                binaryRepresentation[i] = '1'
        resultComplement = '0b'

        for i in binaryRepresentation:
            resultComplement += i
        
        return int(resultComplement, 2)

n = int(input())
s = Solution()
print(s.findComplement(n))