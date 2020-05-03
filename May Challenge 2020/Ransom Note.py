class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineList = list(magazine)
        for i in ransomNote:
            if(i in magazineList):
                magazineList.remove(i)
            else:
                return False
        return True
            
        