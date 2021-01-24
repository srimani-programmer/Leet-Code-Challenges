class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        total_result = roman_dict[s[-1]]
        
        for i in range(len(s)-1, 0, -1):
            
            curr_val = roman_dict[s[i]]
            left_val = roman_dict[s[i-1]]
            
            if(curr_val > left_val):
                total_result -= left_val
            else:
                total_result += left_val
            
        return total_result
                