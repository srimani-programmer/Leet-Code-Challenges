# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool

def isBadVersion(version):pass

class Solution:
    def firstBadVersion(self, n):
        
        low = 1
        high = n
        isBad = -1
        while(low <= high):  

            mid = (low + high) // 2
            if(isBadVersion(mid)):
                high = mid - 1
                isBad = mid
            else:
                low = mid + 1
                 
        return isBad
                
